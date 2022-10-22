from tweepy import StreamingClient

from com.petmedic.utils import Log


class PetMedicTweets(StreamingClient):

    def __init__(self, bearer_token, on_tweet):
        super(PetMedicTweets, self).__init__(bearer_token)

        self.__onTweet = on_tweet

        if on_tweet is None:
            raise Exception("Meed to pass a function")

    def on_tweet(self, tweet):
        Log.debug(tweet.data)
        self.__onTweet(tweet.data)

    def on_connection_error(self):
        self.disconnect()

    def on_closed(self, response):
        print("connection closed")

    def start(self):
        print("getting tweets")
        self.filter(tweet_fields="created_at")
