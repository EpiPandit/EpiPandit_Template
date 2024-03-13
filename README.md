# Template GitHub Repository for EpiPandit Lab, 
## EpiPandit Lab focuses on quantitative veterinary epidemiology and disease ecology
==============================

Text summarizing your project.

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make setup` or `make conda-create`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third-party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. The naming convention is a date (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `03132024-pranav-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── environment.yml   <- The environment file for reproducing the analysis environment, e.g.
    │                         generated with `conda create -f environment.yml`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to process data
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │
    │   └── visualization  <- Scripts to create exploratory and results-oriented visualizations

--------


## Setup Instructions
------------
1. Clone the repo
2. Create a virtual environment
3. Install the requirements
4. Run the notebooks

```bash
git clone
cd WildAlertModels
make conda-create
conda activate wildalert
make setup
jupyter notebook
```

## Run the WNDP Model API
```bash
# src/app/main.py -> change the model checkpoint as CKPT_PATH
uvicorn src.app.main:app --reload

# Visit: localhost:8000/predict/docs

# sample query to the model API
curl -X 'POST' \
  'localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text": "Fell from nest. fall, underweight, nestling. GI / Vent: scant greenish stool, some dried stool on feet and abdomen. energetic"}'

# sample response
{
  "prediction":["gastrointestinal_disease"],
  "scores":
    {
      "clinically_healthy":0.000958,
      "dermatologic_disease":0.001603,
      "gastrointestinal_disease":0.998104,
      "hematologic_disease":0.001031,
      "neurologic_disease":0.000643,
      "nonspecific":0.001958,
      "nutritional_disease":0.002134,
      "ocular_disease":0.000980,
      "physical_injury":0.002120,
      "respiratory_disease":0.001215,
      "urogenital_disease":0.000677
    }
}
```



<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.</small></p>
