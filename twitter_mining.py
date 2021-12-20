import tweepy
import json
import open_key


def process_or_store(tweet):
    print(json.dumps(tweet))


for status in tweepy.Cursor(open_key.api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)

for friend in tweepy.Cursor(open_key.api.get_friends).items():
    process_or_store(friend._json)

for tweet in tweepy.Cursor(open_key.api.user_timeline).items():
    process_or_store(tweet._json)
