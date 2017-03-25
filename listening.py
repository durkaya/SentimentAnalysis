import tweepy
import json


class StreamListener(tweepy.StreamListener):
    def on_connect(self):
        print("Tweet streaming begin.")

    def on_error(self, status):
        print('Error Type: ' + status)
        return False

    def on_data(self, raw):
        data = json.loads(raw)
        fs = open("tweets.txt", "a")

        try:
            print(data, '\n\n\n\n')
            print((data["user"]["screen_name"], data["text"]), '\n')
            if data["retweet_count"]  > 0:
                text = data["text"].split(' ', 2)
                username = data["entities"]["user_mentions"]["screen_name"]
                fs.write(username + ' said that ' + text[1] + ' ' + data["retweet_count"] + ' \n\n\n')
            else:
                fs.write(data["user"]["screen_name"] + ' said that ' + data["text"] + ' \n\n\n')
            fs.close()
        except Exception as e:
            print(e)
        return True


