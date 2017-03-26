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
            if data["text"].find('RT @') is -1:
                username = data["user_mentions"]["screen_name"]
                str1 = 'RT @' + username + ': '
                text = data["text"].strip(str1)
                fs.write(username + ' said that ' + text + '\n\n\n')
                print(username + ' said that ' + text + '\n\n\n')
            else:
                fs.write(data["user"]["screen_name"] + ' said that ' + data["text"] + ' \n\n\n')
            fs.close()
        except Exception as e:
            print(e)
        return True


