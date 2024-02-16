# Analytics

> 💎 End-to-end Data Science and Advanced Analytics Experience 🚀

## Project Organization

> 🛠 Production-grade project template that incorporates best practices for successful Data Science or Machine Learning projects 🚀

```
├── Makefile           <- FIXME: Makefile with convenience commands like `make data` or `make train`
├── README.md          🤝 Explain your project and its structure for better collaboration.
├── config/
│   └── logging.config.ini
├── data               🔍 Where all your raw and processed data files are stored.
│   ├── external       <- Data from third-party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, unprocessed, immutable data dump.
│
├── docs               📓 A default docusaurus || mkdocs project; see docusaurus.io || mkdocs.org for details
│
├── models             🧠 Store your trained and serialized models, model predictions, or model summaries - for easy access and versioning.
│
├── notebooks          💻 Jupyter notebooks for exploration and visualization.
│   ├── analytics-data_exploration.ipynb
│   ├── analytics-data_preprocessing.ipynb
│   ├── analytics-model_training.ipynb
│   └── analytics-model_evaluation.ipynb
│
├── pyproject.toml     <- FIXME: Project configuration file with package metadata for analytics
│                         and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            📊 Generated analysis (reports, charts, and plots) as HTML, PDF, LaTeX.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   🛠 The requirements file for reproducing the analysis environment, for easy environment setup. `pip freeze > requirements.txt`
│
├── setup.cfg          <- FIXME: Configuration file for flake8
│
├── src                💾 Source code for data processing, feature engineering, and model training.
│   ├── data/
│   │   └── data_preprocessing.py
│   ├── features/
│   │   └── feature_engineering.py
│   ├── models/
│   │   └── model.py
│   └── utils/
│       └── helper_functions.py
├── tests/
│   ├── test_data_preprocessing.py
│   ├── test_feature_engineering.py
│   └── test_model.py
├── setup.py           🛠 A Python script to make the project installable.
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── analytics          🧩 Source code for use in this project.
    │
    ├── __init__.py    <- Makes analytics a Python module
    │
    ├── data           <- Scripts to download, preprocess, or generate data
    │   └── make_dataset.py
    │
    ├── features       <- Scripts to turn raw data into features for modeling
    │   └── build_features.py
    │
    ├── models         <- Scripts to train models and then use trained models to make predictions.           
    │   ├── predict_model.py
    │   └── train_model.py
    │
    └── visualization  <- Scripts to create exploratory and results-oriented visualizations
        └── visualize.py
```