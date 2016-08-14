from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


access_token = "2165237045-yITzApHT36KYYRlFNQka26EAKwbjym2zdOLJz3Y"
access_token_secret = "bGuwH8ViHDtYbpRd7T4YrtCypg0jxQn02Qze9TvgnFzVE"
consumer_key = "3Svc7udfX5FXaRl5iJCg9VrhQ"
consumer_secret = "7m324dO7Ho8vue86OJb6yXeJW46BeYXf3JHIqOiRwN8wcO3khD"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['corn', 'soybean', 'wheat'])