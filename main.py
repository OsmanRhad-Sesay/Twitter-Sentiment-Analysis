import tweepy
from textblob import TextBlob
import sys

def app():
    keys = open('keys.txt', 'r').read().splitlines()

    api_key = keys[0]
    secret_api_key = keys[1]
    access_token = keys[2]
    secret_access_token = keys[3]

    api_key = "x"
    secret_api_key = "x"
    access_token = "x"
    secret_access_token = "x"

    auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=secret_api_key)
    auth_handler.set_access_token(access_token, secret_access_token)

    api = tweepy.API(auth_handler)

    search_term = input("Please enter the term you when to search Twitter for: ")
    tweet_number = 200

    tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang='en').items(tweet_number)

    polarity = 0

    positive = 0
    negative = 0
    neutral = 0

    for tweet in tweets:
        text = tweet.text.replace('RT', '')
        if text.startswith(' @'):
            position = text.index(':')
            text = text[position+2:]
        if text.startswith('@'):
            position = text.index(' ')
            text = text[position+2:]
        analysis = TextBlob(text)
        polarity += analysis.polarity
        tweet_polarity = analysis.polarity
        if tweet_polarity > 0.00:
            positive += 1
        elif tweet_polarity < 0.00:
            negative += 1
        elif tweet_polarity == 0.00:
            neutral += 1
        polarity += tweet_polarity
        print(text)

    print(polarity)

    print(f'Amount of positive tweets: {positive}')
    print(f'Amount of negative tweets: {negative}')
    print(f'Amount of neutral tweets: {neutral}')


app()