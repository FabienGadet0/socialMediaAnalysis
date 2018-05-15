#!/usr/bin/python3

import tweepy
import time
from tweepy import OAuthHandler
import sys


consumer_key = 'iHrwgD3YzLCq5PXC46fjg31SO'
consumer_secret = 'tY9UbVKzW1ZuPzP91T1p4IcE5uVtbyXTdtXeUrIveHkSnEXGwa'
access_token = '995594477644361733-PC764WYWgRs3ef0Ifhe1EtABJMBv6rO'
access_secret = 'TnL0BoNTvvAJlYnnNwubCBSyDxghnfuDgE56EITGu5XJx'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
if(api.verify_credentials):
    print ('Connected to the twitter API')

def get_profile(name):
    try:
        user = api.get_user(screen_name = name)
        print(user.name)
    except:
        print('timeOut')

def get_tweet(name, count = 100):
    # name = "result/" + name
    try:
        file = open(name, 'w')
        timeline = api.user_timeline(screen_name=name, count=count)
        # print(timeline.name)
        for tweet in timeline:
        # file.write ("%s\n"  % tweet.created_at)
            file.write ("\n%s\n"  % tweet.text)
        print('finished, all results are written in the file' , name)
    except:
        print ('Error , check your connection')

if __name__ == '__main__':
    try:
        for name in sys.argv[1:]:
            get_tweet(name = name)
    except KeyboardInterrupt:
        quit()