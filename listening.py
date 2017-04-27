import tweepy
import json
from textblob import TextBlob


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
                sample = TextBlob(text)
                polarity = sample.sentiment.polarity
                subjectivity = sample.sentiment.subjectivity
                print(tweet_id + '\t' + time + '\t' + username + '\n' + text + '\n' +
                      'Sentiment Result: polarity=' + str(polarity) +
                      ', subjectivity' + str(subjectivity) + '\n\n')
                fs.write(tweet_id + '\t' + time + '\t' + username + '\n' + text + '\n' +
                         'Sentiment Result: polarity=' + str(polarity) +
                         ', subjectivity' + str(subjectivity) + '\n\n')
            fs.close()
        except Exception as e:
            print(e)
        return True
