
import tweepy
import time
from tweepy import OAuthHandler
import sys
import json

consumer_key = 'iHrwgD3YzLCq5PXC46fjg31SO'
consumer_secret = 'tY9UbVKzW1ZuPzP91T1p4IcE5uVtbyXTdtXeUrIveHkSnEXGwa'
access_token = '995594477644361733-PC764WYWgRs3ef0Ifhe1EtABJMBv6rO'
access_secret = 'TnL0BoNTvvAJlYnnNwubCBSyDxghnfuDgE56EITGu5XJx'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)#, parser=tweepy.parsers.JSONParser())


if(api.verify_credentials):
    print ('Connected to the twitter API')

def get_profile(name, file):
    try:
        user = api.get_user(screen_name = name, count = 1)
        # user = json.dumps(user)
   
        file.write ("name :%s\nlocation : %s\npic : %s\nfriend count : %i \ndescription : %s\nurl : %s\n\n" % (user.name, user.location, user.profile_image_url_https, user.friends_count, user.description, user.url))
    except:
        print('error profile', sys.exc_info()[0])

def get_tweet(name, file, count = 100):
    try:
        # timeline = json.loads(json.dumps(api.user_timeline(screen_name=name, count= count)[0]))
        timeline = api.user_timeline(screen_name=name, count= count,tweet_mode='extended')
        for tweet in timeline:
            file.write ("%s\n"  % tweet.full_text)
    except:
        print ('Error tweets', sys.exc_info()[0])
 
if __name__ == '__main__' :
    try:
        for name in sys.argv[1:]:
            file = open(name, 'w')
            get_profile(name = name, file = file)
            get_tweet(name = name, file = file)
            print('finished')
    except KeyboardInterrupt:
        quit()