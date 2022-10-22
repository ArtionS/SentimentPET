import boto3

from com.petmedic import properties

client = boto3.client(
    service_name='comprehend',
    region_name=properties.region_name
)


def get_dominant_language(tweet):
    language = client.detect_dominant_language(
        Text=tweet
    )
    return language


def get_sentiment(tweet, language_code):
    response = client.detect_sentiment(
        Text=tweet,
        LanguageCode=language_code
    )

    del response["ResponseMetadata"]
    # del response["RetryAttempts"]

    return response
