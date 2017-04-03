
from pymongo import MongoClient
import tweepy
import json

# MongoDB connection is established and configured
connection = MongoClient('localhost', 27017)
db = connection.StreamData
db.tweets.create_index("id", unique=True, dropDups=True)
collection = db.tweets

# organizing tweet information
class StreamListener(tweepy.StreamListener):

    def on_connect(self):
        print("Tweet streaming begin.")

    def on_error(self, status):
        print('Error Type: ' + status)
        return False

    def on_data(self, raw):
        data = json.loads(raw)
        tweet_id = data['id_str']  # The ID of tweet from Twitter in string format
        time = data['created_at']  # The time of creation of the tweet
        username = data['user']['screen_name']  # The Tweet author's username
        text = data['text']  # The entire body of the Tweet


        try:
            if data["text"].find('RT @') is -1:  # if not exist
                # Create object in json format
                tweet = {'id': tweet_id, 'created_at': time, 'username': username, 'text': text}
                # Pretty print
                print(json.dumps(tweet, indent=4, sort_keys=True))
                # Insert Tweet data to MongoDB
                collection.save(tweet)
        except Exception as e:
                    print(e)
        return True
