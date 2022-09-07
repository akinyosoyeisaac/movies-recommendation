import pandas as pd
import yaml

# loading the configuration parameters
with open("params.yaml") as f:
    config = yaml.safe_load(f)

def recommender(title, min_count=0):

    """
    title: str = title of that has been watched or liked by a user
    min_count: int = the minimum number of movies that has voted for. Default 0

    """
    # transform data with column movie_id, index as user_id and value as rating
    df_p = pd.read_csv(config["paths"]["clean_data_t"]).set_index("customer_id")
    df_p.columns.name = "movie_id"
    
    # importing the movie titles
    movies_title = pd.read_csv(config["paths"]["movie_title"], encoding = "ISO-8859-1", header = None, names = ['Movie_Id', 'Year', 'Name'])
    
    # function to parse the title and movie name in movies_title
    to_lower = lambda x: x.lower()

    # grouping of the training file by movie_id with the count and mean
    df_movie_summary = pd.read_csv(config["paths"]["movie_summary"]).set_index("movie_id")
    
    
    # checking if the movie title exist in our database
    if title.lower() in movies_title["Name"].apply(to_lower).to_list():
        # if it exist the code below is executed
        # extracting the movie id from the movies_title file
        i = int(movies_title.Movie_Id[movies_title['Name'].apply(to_lower) == title.lower()])
        # extracting the all customer that has voted for movie
        target = df_p[str(i)]
        # calculating the corelation matrix between the users that has voted for the movies and users that voted for other movies
        similar_to_target = df_p.corrwith(target)
        # coverting the correlation matrix into a dataframe
        corr_target = pd.DataFrame(similar_to_target, columns = ['PearsonR'])
        # dropping the nan values
        corr_target.dropna(inplace = True)
        # sorting the values from the highest correlation to the least correlation
        corr_target = corr_target.sort_values('PearsonR', ascending = False)
        # set the index to interger
        corr_target.index = corr_target.index.map(int)
        # concatenating the corr_target, movie_title and df_movie_summary
        corr_target = corr_target.join(movies_title.set_index("Movie_Id")).join(df_movie_summary)[['PearsonR', 'Name', 'count', 'mean']]
        # returning the first ten related movies with a particular number of movie count
        return corr_target[corr_target['count']>min_count][1:6].reset_index()["Name"].to_dict()
    else:
        # if movies does not exist in the database the response that will be given
        return "Please check the title you have provided to see if it is correct or the title does not exist in our database"
    
