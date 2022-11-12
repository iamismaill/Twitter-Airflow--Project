import tweepy
import pandas as pd 
import json 
from datetime import datetime 
import s3fs


##our paramaters

access_key ="NARLXHvbYNhTPlJ7v0ZxKBj3P"
acces_secret = "ky3QpFnT7t46arrj4YoX4yzy5HpB3hHmYX11APaxwxDYoXmGAZ"
consumer_key ="1589170115157053440-pQkFRzG9dAem0qgwV6zS8LPtaZBc4Y"
consumer_secret="YWgOh171MvWWBWtIOjHKLK6s3DxZMacKFHubNdYqLoOXr"

##twitter authentication 
##time to create connection between my app and twitter api
auth = tweepy.OAuthHandler(access_key,acces_secret)
auth.set_access_token(consumer_key,consumer_secret)
api = tweepy.API(auth)
##Api Object 
tweets = api.user_timeline(screen_name='@iamismail__', 
                            # 200 is the maximum allowed count
                            count=10,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )
tweet_list =[]
for tweet in tweets :
    text = tweet._json["full_text"]
    
    refined_tweeet  = { "user":tweet.user.screen_name,
                        'text' :text,
                        'favourite_count':tweet.favorite_count,
                        'retweet_count':tweet.retweet_count,
                        'created_at':tweet.created_at}
            
    tweet_list.append(refined_tweeet)
##conver the list into dataframe 

df = pd.DataFrame(tweet_list)
##save intocsvfile
df.to_csv("ismail_twitter.csv")