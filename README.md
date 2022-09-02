# movies-recommendation
# Content-Based-Movie-Recommender-System
It is a common thing in this new era where technology is fast evolving and humanity is constantly been faced with various challenges the requires devoting a lot time. He then need to leave some task to the process of automation and one of such task is a recommendation system. No one wants to waste time surfing a amazon or boom-player in service for a product or musics of interest. Such task can be left to one of the sub of AI which is recommendation system.
This project uses a user-item collaborative algorithm, and a Pearson correlation algorithm to build a movies recommendation systems using the a datasets gotten from Kaggle links can be gotten from below.  
A recommendation system is used to automate the process of recommending things to a user based on his\her past interest or likes. for example, YouTube and NetFlix uses a recommendation system to automatically suggest movies and videos to users based on their past preference. There are different types of recommendation system such as Popularity based,Content based, Collaborative filtering and Hybrid.



# TOOLS
___In this project the following python libraries were used___


[![pandas](https://img.shields.io/badge/Pandas-green.svg?style=flat&logo=pandas&logoColor=white)](http://pandas.pydata.org/doc/)
[![Numpy](https://img.shields.io/badge/Numpy-red.svg?style=flat&logo=numpy&logoColor=white)](http://numpy.org/doc/stable/)
[![Sklearn](https://img.shields.io/badge/Sklearn-green.svg?style=flat&logo=scikit-learn&logoColor=white)](http://scikit-learn.org/stable/modules/classes.html)
[![Matplotlib](https://img.shields.io/badge/matplotlib-yellow.svg?style=flat&logo=matplotlib&logoColor=white)](http://matplotlib.org/stable/api/index.html)
[![FastAPI](https://img.shields.io/badge/fastapi-yellow.svg?style=flat&logo=fastapi&logoColor=white)](http://matplotlib.org/stable/api/index.html)
[![Surprise](https://img.shields.io/badge/scikit-surprise-yellow.svg?style=flat&logo=scikit-surprise&logoColor=white)](https://www.surpriselib.com)


## Setup to Run

> In this project two models were built the first using the collaborative filtering algorithm(Probabilistic Matrix Factorization for the surprise library) and the other was the Pearson correlation using the pandas library
>
> All codes included in both the notebooks and the scripts are configured to run from the root directory 
>
> All libraries used in building this project has been included in the requirement.txt in the root directory <a href="requirements.txt"> libraries </a>
```
python
pip install -r requirements.txt
```

> For this purpose of training given that the files where large files only combined_data_1.txt and movies_titles.csv where used in the course of the training
>
> The two files should be in the **./data/raw** <a href="data/raw">Directory</a>
>
> For more on data visit the <a href="#Dataset used">Datasets used</a>

## Model performance
> The Model was cross validated on a five fold split and below is the performance
<img src="reports\figures\svd_model_performance.JPG" width="350">

## Datasets used

* The datasets used for this project can be gotten [here](https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data)
* The Kaggle data consist of five datasets the first four includes combined_data_[1-4].txt and the movies_titles.csv which are very large files hence, they are not included in this git repository to work along side this project you should download the file from the Kaggle link above

## Deployment
1. The model was wrapped around an API using FastAPI though the model has not be deployment for the same reason the training files were not included in this repository
2. In future we hope to explore other solution of overcoming this limitation such as using Azure, Google Service and DVC to manage this kind of project
## Others
1. [Medium post](https://medium.com/@tonmeje/490645fdb143)
Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- First stage of cleaning which is to convert the combined_data_1.txt to a structured csv file data1.csv
    │   ├── processed      <- The final, canonical data sets for modeling. consist of four files data_clean_transpose.csv, data_clean.csv, df_cust_summary.csv, df_movie_summary.csv
    │   └── raw            <- The original, immutable data dump. combined_data_1.txt, movie_titles.csv
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as jpg.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
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
    └── params.yaml <- Parameter used in training
