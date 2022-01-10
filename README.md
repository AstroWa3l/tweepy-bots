# How to set up a twitter bot using python's tweepy library

## Create a twitter developer account and project

***Make sure you are logged into your twitter account that you want to link to your bot***

Steps:

1. Go to [Twitter developer platform](https://developer.twitter.com/)
2. Click on the "Sign up" button
3. Fill out the form  and then proceed to agree to sign away your rights to twitter lmao
4. Verify Email
5. Create App Name
6. Get your keys and store them into a csv or however you would like (for this guide we use a csv file)

#### Here is how I have set up my csv file for keys:

| Type                | Secret Key   |
|---------------------|--------------|
| key                 | ***********  |
| secret              | ***********  |
| token               | ***********  |
| access_token        | ***********  |
| access_token_secret | ***********  |

For clarification:

Consumer API Key = key 

Consumer API Secret = secret 

Bearer Token = token

Access Token = access_token 

Access Token Secret = access_token_secret



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
