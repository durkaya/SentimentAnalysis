from pymongo import MongoClient
import tweepy
import json

connection = MongoClient('localhost', 27017)
db = connection.StreamData
db.tweets.ensure_index("id", unique=True, dropDups=True)
collection = db.tweets


class StreamListener(tweepy.StreamListener):

    def on_connect(self):
        print("Tweet streaming begin.")

    def on_error(self, status):
        print('Error Type: ' + status)
        return False

    def on_data(self, raw):
        data = json.loads(raw)
        tweet_id = data['id_str']  # The ID of tweet from Twitter in string format
        username = data['user']['screen_name']  # The Tweet author's username
        text = data['text']  # The entire body of the Tweet

        try:
            print(data, '\n', (data["user"]["screen_name"], data["text"]), '\n\n\n\n')
            if data["text"].find('RT @') is -1:
                tweet = {'id': tweet_id, 'username': username, 'text': text}
                # Insert Tweet data to MongoDB
                collection.save(tweet)
        except Exception as e:
                    print(e)
        return True