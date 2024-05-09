import json
import boto3
import time
s3_client = boto3('s3')

def lambda_handler(event, context):
    # TODO implement
    try:
        print("Event data", event)
        if "body" in event and event["body"] != None:
            
            payload = json.loads(event["body"])
            print("payload = ",payload)
            current = int(time.time())
            file_name = f"sensor_data_{current}.json"
            bucket_name = "sensordatabyarun"
            s3_client.put_object(
                 Body = json.dumps(payload),
                 Bucket = bucket_name,
                 key = file_name
            )

            return {
                        'statusCode': 200,
                        'body': json.dumps(
                        {
                            "message" : "Data updated Successfully in S3"
                        })
                        
                        
                    }
        else:
                return {
                            'statusCode': 400,
                            'body': json.dumps(
                                {
                                    "message" : "BAD REQUEST, Body shall not be Empty"
                                })
                        }
    except Exception as e:
        print(e)
        return {
                            'statusCode': 500,
                            'body': json.dumps(
                                {
                                    "message" : "Server failed to handle to request"
                                })
                        }
