import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    DF = tweets[tweets['content'].str.len() > 15]
    return DF[['tweet_id']]
    