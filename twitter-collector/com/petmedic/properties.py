
import os

tw_app_secret_name = os.getenv("SECRETS_KEY", "prod/twitter/petmedicdusc")

raw_twitter_to_s3 = os.getenv("FIREHOSE_STREAM_NAME", "twitts-to-s3")
analysed_twitter_to_s3 = os.getenv("FIREHOSE_STREAM_NAME", "analysed-to-s3")

region_name = "us-east-1"

log_level = "debug"
