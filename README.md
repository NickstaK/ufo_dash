UFO Dash Dashboard

A minimal dashboard for exploring UFO sightings data with Streamlit.

Prerequisites:

Python 3.8+ installed
Git installed

Dataset:

Raw dataset available from NUFORC on Kaggle: https://www.kaggle.com/datasets/NUFORC/ufo-sightings

Setup:

Clone the repository: git clone git@github.com:NickstaK/ufo_dash.git cd ufo_dash

Create and activate a virtual environment: python3 -m venv .venv source .venv/bin/activate

Install dependencies: pip install -r requirements.txt

Usage:

Place raw data: download the CSV from Kaggle and save it as data/raw/complete.csv

Clean and prepare data: python data/scripts/clean_raw.py

Launch the Streamlit dashboard: streamlit run app.py

The dashboard will be available at http://localhost:8501.
