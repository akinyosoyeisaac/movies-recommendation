import pandas as pd
import yaml

with open("params.yaml") as f:
    config = yaml.safe_load(f)

def recommender(title, min_count):

    df_p = pd.read_csv(config["paths"]["clean_data_t"]).set_index("customer_id")
    df_p.columns.name = "movie_id"
    
    movies_title = pd.read_csv(config["paths"]["movie_title"], encoding = "ISO-8859-1", header = None, names = ['Movie_Id', 'Year', 'Name'])
    
    to_lower = lambda x: x.lower()
    
    df_movie_summary = pd.read_csv(config["paths"]["movie_summary"]).set_index("movie_id")
    
    
    if title.lower() in movies_title["Name"].apply(to_lower).to_list():
        i = int(movies_title.Movie_Id[movies_title['Name'].apply(to_lower) == title.lower()])
        target = df_p[str(i)]
        similar_to_target = df_p.corrwith(target)
        corr_target = pd.DataFrame(similar_to_target, columns = ['PearsonR'])
        corr_target.dropna(inplace = True)
        corr_target = corr_target.sort_values('PearsonR', ascending = False)
        corr_target.index = corr_target.index.map(int)
        corr_target = corr_target.join(movies_title.set_index("Movie_Id")).join(df_movie_summary)[['PearsonR', 'Name', 'count', 'mean']]
        return corr_target[corr_target['count']>min_count][:10].reset_index()["Name"].to_dict()
    else:
        return "Please check the title you have provided to see if it is correct or the title does not exist in our database"
    
