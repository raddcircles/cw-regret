#!/usr/bin/python
import configparser, os, sys, tweepy
from termcolor import colored
config = configparser.ConfigParser()
config.read('creds.ini')
game_name = input("Please enter the game name (Use normal scene writing, do not include a dash or the release group):")
release_group = input("Please enter the short form of the release group (do not include a dash): ")
thread_link = input("Please enter the discussion thread link:")
def twitter():
    twitter_access_key = config.get('Twitter', 'Twitter_Access_Key')
    twitter_access_secret = config.get('Twitter', 'Twitter_Access_Secret')
    twitter_consumer_key = config.get('Twitter', 'Twitter_Consumer_Key')
    twitter_consumer_secret = config.get('Twitter', 'Twitter_Consumer_Secret')
    if twitter_access_key == "replace_me" or twitter_access_secret == "replace_me" or twitter_consumer_key == "replace_me" or twitter_consumer_secret == "replace_me":
        print(colored("read the docs, idiot", 'red'))
        sys.exit()
    try:
        auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
        auth.set_access_token(twitter_access_key, twitter_access_secret)
        api = tweepy.API(auth)
        print(api.me().name)
        twitter_results = game_name + "-" + release_group + "\n" + thread_link + " #crackwatch #denuvo"
        api.update_status(status=twitter_results)
        return("updated twitter status: %s" % twitter_results)
    except:
        print(colored("Invalid Twitter Credentials!", "red"))
        sys.exit()
exectwitter = twitter()