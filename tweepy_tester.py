#twitterAPI test

#set keys/tokens
consumer_key = '5sF083PsI7PtIvzYnjtpyhlnw'
consumer_secret = 'GMvqufwMwl8SzcunKPYiklBbyrrMt67ZKUEn7QPkwKhtnXBNkg'

access_token = '96582228-j9QUt0J9mKjYFlu0t0q1xlBKUCnXqujIXJMcdIxMC'
access_token_secret = 'e1PMM6gPYShkC5GlZvx4dj7wxnKwvpB61rRWcdmV4PuBj'

#start Tweepy and do autorization
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
