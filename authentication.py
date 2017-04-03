import tweepy
from tweepy import OAuthHandler
import listening

#twitter api keys to authanticate
consumer_key = "dtKTW35ISxLtPDCszilhNk6R2"
consumer_secret = "pDoisuGvzTGYte5rNEtjguiixVyys0IrL98xu5tzxE7aG8KZCJ"

access_token = "773843946-LBFza4JmUOrzrUOkahDdtHXi6AHwFQyjwH6j7Ibg"
access_token_secret = "JU0ExxNVFkQbBzipW0EOL9Lkb6dm3RadGdfoJeaLdOUgm"

#authentication sections
auth = OAuthHandler(consumer_key, consumer_secret)
print("First auth done")
auth.set_access_token(access_token, access_token_secret)
print("2nd auth done")

#tracked word
WORDS = ['iphone']

#from listening library, StreamListener object created
listener = listening.StreamListener(api=tweepy.API(wait_on_rate_limit=True))
#from tweepy library, Stream begins
streamer = tweepy.Stream(auth=auth, listener=listener)

print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS, languages=["en"]) #filtering keywords