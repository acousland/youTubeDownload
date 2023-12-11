#!/bin/bash

# Specify the conda environment name
CONDA_ENV_NAME="videoTranscribe"

# Activate the conda environment
source $(conda info --base)/etc/profile.d/conda.sh
conda activate $CONDA_ENV_NAME

# Run your command
streamlit run ui.py