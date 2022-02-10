# How to set up a twitter bot using python's tweepy library

## Create a twitter developer account and project

***Make sure you are logged into your twitter account that you want to link to your bot***

Steps:

1. Go to [Twitter developer platform](https://developer.twitter.com/)
2. Click on the "Sign up" button
3. Fill out the form  and then proceed to agree to sign away your rights to twitter lmao
4. Verify Email
5. Create App Name
6. Get your keys and store them safely (for this guide we use a .env file)


For clarification my keys are stored in a .env file as follows:

Consumer API Key = KEY 

Consumer API Secret = SECRET 

Bearer Token = TOKEN

Access Token = ACCESS_TOKEN 

Access Token Secret = ACCESS_TOKEN_SECRET



## Install needed python libraries

```python
pip install tweepy pandas
```

## Create a new folder for the bot, any media and your keys

```bash
mkdir tweepy-bots
cd tweepy-bots
```
## Create a new file called `keys.csv` and put your keys in it as I have done above

```bash
touch keys.csv
```

## Create a new file called `twitterbot.py`

```bash
touch twitterbot.py
```
- Now we can start writing our code using whatever editor we want I use VS Code XD but for simplicity let's use nano in this guide.

```bash
nano twitterbot.py
```
#### First thing we need to do is import the libraries then set up our authentication

```python
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

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
```

#### Next we create the code to update status (aka tweeting)

- Lets make a variable to hold our tweet's text

```python
text = """How efficient is #Cardano ? 

Over 200 blocks on these two solar panels wired in series. 

14 watts to power the pool. 

Absolutely no reason to stake inside a datacenter. Thats called centralization. 

What do we want?  #TrueDecentralization and network resilience."""

```
- Now we need to upload the media to twitter using the chunked uploader feature

```python
media_filename = os.path.join(here, 'centered-star-forge.gif')

chunked_media = api.chunked_upload(filename=media_filename, media_category='tweet_gif')
```
- Now we can update the status with the media and our text
```python
update_status = api.update_status(status=text, media_ids=[chunked_media.media_id])
```

### The last thing we need to do now is set up our cron job to run our code on our schedule

- We will run the script once a day at 9am everyday

Open up a terminal and run the following command to check if you have cron jobs running:

```bash
crontab -l
```

If you don't have any cron jobs running, then you can add a new cron job by this command:

```bash
crontab -e
```
This will open a VIM based text editor for you to add your cron job to the cron job file.

We need to know our path for python package on our machine so we can run our code and you can find that by typing following command and then copy the path:
```bash
which python
```

you simply need to add the following line to the cron job file (use absolute paths):
```bash
0 9 * * * /User/wael/opt/anaconda3/bin/python /home/username/tweepy-bots/twitterbot.py
```

Now you can open terminal and run the following command to check if your cron job is running properly by checking your systems mail:

```bash
cd /var/mail

nano wael
```
