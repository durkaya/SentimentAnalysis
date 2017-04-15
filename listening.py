import tweepy
import json
from processes import tokenize_process


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
        fs = open("tweets.txt", "a")

        try:
            # insert tweet data to tweet.txt file if RT is not exist
            if data['text'].find('RT @') is -1:
                fs.write(tweet_id + '\n' + time + '\n' + username + '\n' + text + '\n\n\n')
                print(tweet_id + '\n' + time + '\n' + username + '\n' + text + '\n')
                print(tokenize_process(tweet_id, text) + '\n\n\n')  # tokenize tweets
            fs.close()
        except Exception as e:
            print(e)
        return True
