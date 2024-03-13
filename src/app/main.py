from typing import Dict, List, Optional

import torch
import torch.nn.functional as F
import transformers
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    PretrainedConfig,
)

transformers.logging.set_verbosity_error()


class Model:
    def __init__(self, ckpt_path) -> None:
        torch.set_num_threads(1)
        torch.set_grad_enabled(False)

        self.tokenizer = AutoTokenizer.from_pretrained(ckpt_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            ckpt_path,
        )
        self.config = PretrainedConfig.from_pretrained(ckpt_path)
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu",
        )
        self.model = self.model.to(self.device)

    def _pre(self, text: str) -> dict:
        tokens = self.tokenizer(text, return_tensors="pt")
        tokens = {k: v.to(self.device) for k, v in tokens.items()}
        return tokens

    def _infer(self, tokens: dict):
        outputs = self.model(**tokens)
        return outputs

    def _post(self, outputs):
        probs = F.sigmoid(outputs.logits.squeeze().detach().cpu())
        preds = (probs > 0.5).int()
        labels = [
            self.config.id2label[idx]
            for idx, label in enumerate(preds)
            if label == 1.0
        ]
        scores = {
            self.config.id2label[idx]: round(prob.item(), 6)
            for idx, prob in enumerate(probs)
        }
        return labels, scores

    def predict(self, text: str) -> List[str]:
        tokens = self._pre(text)
        outputs = self._infer(tokens)
        preds, scores = self._post(outputs)
        return preds, scores


CKPT_PATH = "notebooks/wndp-exp/checkpoint-1500"  # Pass the checkpoint location of saved model weights
model = Model(ckpt_path=CKPT_PATH)

app = FastAPI()


class Message(BaseModel):
    text: Optional[str] = "test"


@app.post("/predict")
async def predict(msg: Message):
    preds, scores = model.predict(msg.text)
    return {"prediction": preds, "scores": scores}


@app.get("/")
async def run_health_check():
    return {"WNDP Model API": True}
