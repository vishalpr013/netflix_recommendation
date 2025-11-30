Netflix Recommendation — Project README
======================================

Project overview
----------------
This repository contains an end-to-end movie recommendation demo built from public TMDb-derived CSVs. It includes a Jupyter notebook (`movie_recommendation.ipynb`) that explores the dataset and demonstrates a collaborative/content-based hybrid recommendation approach, and a minimal Flask app (`app.py`) to serve recommendations locally.

Repository contents
-------------------
- `app.py` — Small Flask web app that loads the prepared movie data and exposes a recommendation endpoint for demoing locally.
- `movie_recommendation.ipynb` — Notebook with EDA, feature extraction, similarity calculations, and evaluation notes.
- `tmdb_5000_credits.csv`, `tmdb_5000_movies.csv` — Raw CSV datasets (from the TMDb 5000 dataset) used to build the recommendation engine.

Key goals
---------
- Demonstrate building a lightweight content / hybrid movie recommender using real-world metadata (genres, cast, crew, keywords).
- Provide a runnable demo via `app.py` to quickly query recommendations.
- Offer reproducible instructions to re-run the notebook and refresh the model/data.

Prerequisites
-------------
- Python 3.8+ environment (3.10 recommended).
- Create an isolated environment (venv or conda).
- Install dependencies. If a `requirements.txt` isn't present, install commonly used packages below.

Recommended packages
--------------------
At minimum install:
- pandas
- numpy
- scikit-learn
- flask
- jupyter
- nltk (if the notebook uses text normalization/tokenization)

Quick setup (PowerShell)
------------------------
1. Create and activate a virtual environment:

   python -m venv .venv; .\.venv\Scripts\Activate.ps1

2. Install packages (example):

   python -m pip install --upgrade pip; pip install pandas numpy scikit-learn flask jupyter

3. Start Jupyter to run the notebook or run the Flask demo app:

   jupyter lab
   # or to run app.py
   python app.py

How to use
----------
- Notebook: Open `movie_recommendation.ipynb` and run cells sequentially. Key sections include data merging (`tmdb_5000_movies.csv` + `tmdb_5000_credits.csv`), feature engineering (genres, cast, crew parsing), vectorization, similarity computation, and sample recommendations.
- Flask demo: `app.py` loads preprocessed data and exposes one or more endpoints (e.g., `/recommend?title=Inception`). Start it with `python app.py` and open the printed local URL in a browser to test.

Data sources and attribution
----------------------------
The CSV files in this repository are derived from the TMDb 5000 dataset and include movie metadata and credits. If you redistributed or modified these files, please respect TMDb terms and attribution.

Reproducibility notes
---------------------
- Record and reuse random seeds when performing train/test splits or any randomized algorithm.
- If the notebook uses NLTK tokenizers, ensure relevant corpora (stopwords, punkt) are downloaded in the environment.
- Save any intermediate preprocessed artifacts (pickles or CSVs) if you want to quickly start the Flask demo without re-running the notebook.

Improvements & next steps
-------------------------
- Add a small script to precompute and save the similarity matrix for faster demo startup.
- Add unit tests around preprocessing and recommendation logic.
- Add Dockerfile for reproducible deployment.
- Add caching to the Flask app to speed repeated requests.

License & contact
-----------------
This project is intended as an educational demo. Check dataset licensing for production use. For issues or collaboration, contact the repository owner.
