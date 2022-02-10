import tweepy
import random
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

# Twitter API credentials
consumer_api_key = os.getenv("KEY")
consumer_secret_key = os.getenv("SECRET")
consumer_token = os.getenv("TOKEN")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Build the API object with our credentials
auth = tweepy.OAuthHandler(consumer_api_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# verify credentials

def verify_credentials():
        try:
                api.verify_credentials()
                print("Authentication OK")
        except:
                print("Error during authentication")

verify_credentials()

def tweet_with_media(text, filename, media_category):
        
        # make sure inputs are strings if not tell the user
        if type(text) != str or type(filename) != str or type(media_category) != str:
                print("inputs must be strings")
                return
        
        # get our path for working directory and filename
        
        here = os.path.dirname(os.path.abspath('__file__'))
        media_filename = os.path.join(here, filename)
        
        # get chunked media for twitter API upload
        chunked_media = api.chunked_upload(filename=media_filename, media_category=media_category)
        
        # If upload of data successfull we will have a media_id
        print(chunked_media.media_id)
        
        # update status with our text and media
        update_status = api.update_status(status=text, media_ids=[chunked_media.media_id])

# Feel free to change the text
text = """How efficient is #Cardano ? 

Over 200 blocks on these two solar panels wired in series. 

14 watts to power the pool. 

Absolutely no reason to stake inside a datacenter. Thats called centralization. 

What do we want?  #TrueDecentralization and network resilience."""

# feel free to change the filename and media_category
tweet_with_media(text, "your_file_name.gif", "tweet_gif")