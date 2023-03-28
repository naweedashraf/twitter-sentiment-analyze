import tweepy
from textblob import TextBlob

consumer_key = '' #Api Key
consumer_secret = '' #API Key Secret

access_token = '' #Access Token
access_token_secret = '' #Access Token Secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search_tweets('Search Phrase')
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)