MLOps_First_Prediction
==============================

Meu primeiro repositório com flask e predições em Python para MLOps.

Instale se precisar CookieCutter:
    pip install cookiecutter
    https://drivendata.github.io/cookiecutter-data-science/

Deve ter o git
    https://git-scm.com/downloads

Clonar os repositório em: 


Criar o ambiente virtual, indo até a pasta raiz do repositório e rodar:
    No windows:
        venv/Scripts/activate
            caso não rode por falta de permissão no powershell (recomendado):
                Get-ExecutionPolicy
                    se estiver 'Restricted' ou 'AllSigned' rode:
                Set-ExecutionPolicy Unrestricted
                    Escolha opção A (for all)

    No Linux:
        venv/bin/activate

Para utilizar o projeto deve-se primeiramente criar um ambiente virtual e rodar o 'requirements.txt' usando:
    pip install -r requirements.txt

Criar as variáveis de ambiente:
    No Windows: 
        Set-Content -Path BASIC_AUTH_USERNAME -Value 'seuUsuario'
        Set-Content -Path BASIC_AUTH_PASSWORD -Value 'suaSenha'

        teste com:
            Set-Location Env:
                ls
                    e veja de estão lá

    No Linux:
        export BASIC_AUTH_USERNAME=seuUsuario
        export BASIC_AUTH_PASSWORD=suaSenha


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling (OUR DATA ARE HERE).
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries (OUR models.sav ARE HERE)
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`. (OUR NOTEBOOKS ARE HERE)
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │ 
    │   ├── app            <-flask server generating (OUR MAIM APP IS HERE) 
    │   │   └── maim.py
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
