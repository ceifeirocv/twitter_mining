import json
from tweepy import OAuthHandler
import tweepy

with open('../twitter_keys.json') as file_object:
    keys = json.load(file_object)


consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_secret = keys['access_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
