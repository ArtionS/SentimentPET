import boto3
from com.petmedic import properties
from com.petmedic.utils import Log
import json

client = boto3.client(
    service_name='firehose',
    region_name=properties.region_name
    )


def get_str_message(message):
    if isinstance(message, str):
        return message+"\n"

    if isinstance(message, dict):
        return json.dumps(message)+"\n"

    Log.info(f"Unable to get string from: {type(message)}")
    return None


def push_message(stream,  message):
    to_send = get_str_message(message)
    Log.info(f"message: {to_send}")
    client.put_record(
        DeliveryStreamName=stream,
        Record={
            'Data': to_send
        }
    )
