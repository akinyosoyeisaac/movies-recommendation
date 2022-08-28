import pandas as pd
import numpy as np


def recommender(title, min_count):

    df_viewmovies = pd.read_csv(r"data\processed\data1.csv", names= ["movie_id", "customer_id", "rating", "ratingdate"])
    df_viewmovies["rating"] = df_viewmovies["rating"].astype(np.float32)
    df_viewmovies.ratingdate = pd.to_datetime(df_viewmovies.ratingdate)

    f = ['count','mean']

    df_movie_summary = df_viewmovies.groupby('movie_id')['rating'].agg(f)
    movie_benchmark = round(df_movie_summary['count'].quantile(0.8),0)
    keep_movie_list = df_movie_summary[~(df_movie_summary['count'] < movie_benchmark)].index

    df_cust_summary = df_viewmovies.groupby('customer_id')['rating'].agg(f)
    cust_benchmark = round(df_cust_summary['count'].quantile(0.8),0)
    keep_cust_list = df_cust_summary[~(df_cust_summary['count'] < cust_benchmark)].index

    df_viewmovies_copy = df_viewmovies.copy()[df_viewmovies.copy().movie_id.isin(keep_movie_list)]
    df_viewmovies_copy = df_viewmovies_copy[df_viewmovies_copy.customer_id.isin(keep_cust_list)]

    df = df_viewmovies_copy.copy()

    df_p = pd.pivot_table(data=df, values="rating", columns="movie_id", index="customer_id")
    
    movies_title = pd.read_csv(r"data\netflix price data\movie_titles.csv", encoding = "ISO-8859-1", header = None, names = ['Movie_Id', 'Year', 'Name'])
    
    print("For movie ({})".format(title))
    print("- Top 10 movies recommended based on Pearsons'R correlation - ")
    i = int(movies_title.Movie_Id[movies_title['Name'] == title])
    target = df_p[i]
    similar_to_target = df_p.corrwith(target)
    corr_target = pd.DataFrame(similar_to_target, columns = ['PearsonR'])
    corr_target.dropna(inplace = True)
    corr_target = corr_target.sort_values('PearsonR', ascending = False)
    corr_target.index = corr_target.index.map(int)
    corr_target = corr_target.join(movies_title.set_index("Movie_Id")).join(df_movie_summary)[['PearsonR', 'Name', 'count', 'mean']]
    print(corr_target[corr_target['count']>min_count][:10].to_string(index=False))
    
