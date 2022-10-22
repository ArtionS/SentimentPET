from com.petmedic import properties
from com.petmedic.interface.aws.secrets.secrets_manager import get_secret
from com.petmedic.interface.twitter import PetMedicTweets
from com.petmedic.interface.aws.firehose import push_message
from com.petmedic.interface.aws.comprehend import get_sentiment, get_dominant_language


valid_languages_codes = ["ar", "hi", "ko", "zh - TW", "ja", "zh", "de", "pt", "en", "it", "fr", "es"]


def send_tweets_to_raw(message):
    push_message(properties.raw_twitter_to_s3, message)


def send_tweets_to_analysed(message):
    push_message(properties.analysed_twitter_to_s3, message)


def get_main_language(language):
    score = 0
    code = "es"

    for l in language["Languages"]:
        if l["Score"] > score:
            score = l["Score"]
            code = l["LanguageCode"]

    if code in valid_languages_codes:
        return code
    else:
        return "es"


def process_tweets(message):
    print(message)
    send_tweets_to_raw(message)
    language = get_dominant_language(message["text"])
    sentiment = get_sentiment(message["text"], get_main_language(language))
    message["language"] = language["Languages"]
    message["sentiment"] = sentiment
    print(message)
    send_tweets_to_analysed(message)


def get_tweets():
    print("Connecting to twitter")
    pm = PetMedicTweets(get_secret(properties.tw_app_secret_name)["bearer-token"],
                        on_tweet=process_tweets
                        )
    pm.start()
    print("end")

if __name__ == '__main__':
    get_tweets()

