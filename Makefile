help:
	@echo "- conda-create: Create conda environment from environment.yml file"
	@echo "- setup: Initialize git & install pre-commit packages"
	@echo "- clean: Cleans up pycache & ipynb checkpoints"

conda-create:
	mamba env update --prune -f environment.yml

setup:
	git init
	pre-commit install

clean:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ .ipynb_checkpoints .pytest_cache
