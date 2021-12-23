# %%
import tweepy
import pandas as pd
import os

here = os.path.dirname(os.path.abspath(__file__))

filename = os.path.join(here, 'twitter_api_keys.csv')

# Twitter API credentials
key_df = pd.read_csv(filename)
consumer_api_key = key_df[key_df.type == 'key']['Password'].values[0]
consumer_secret_key = key_df[key_df.type == 'secret']['Password'].values[0]
consumer_token = key_df[key_df.type == 'token']['Password'].values[0]
access_token_secret = key_df[key_df.type == 'access_token_secret']['Password'].values[0]
access_token = key_df[key_df.type == 'access_token']['Password'].values[0]

auth = tweepy.OAuthHandler(consumer_api_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


text = """How efficient is #Cardano ? 

Over 200 blocks on these two solar panels wired in series. 

14 watts to power the pool. 

Absolutely no reason to stake inside a datacenter. Thats called centralization. 

What do we want?  #TrueDecentralization and network resilience."""

media_filename = os.path.join(here, 'centered-star-forge.gif')

chunked_media = api.chunked_upload(filename=media_filename, media_category='tweet_gif')
chunked_media.media_id

update_status = api.update_status(status=text, media_ids=[chunked_media.media_id])



