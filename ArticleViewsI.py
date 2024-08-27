import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    DF = views[(views['author_id'] == views['viewer_id'])].rename(columns= {'author_id': 'id'}).drop_duplicates(subset = ["id"], keep= "first").sort_values(by = ['id'])
    
    return DF[['id']]