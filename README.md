# function-bike-rider
This is a repo for showing what you can do with a function


## Setup Cloud Environment (AWS Cloud9)

`python3 -m venv ~/.function-bike-rider`
`source ~/.function-bike-rider/bin/activate`

## SSH Keys

`ssh-keygen -t rsa`

upload to github

## Create Scaffold (with Marco Polo function)

* Makefile
* hello.py
* requirements.txt

## Continuous Integration with Github Actions

* test_hello.py
* installed `pylint`, `pytest`, `black`

## Building a command-line tool

* use click to build a cli

https://github.com/noahgift/function-bike-rider/blob/master/cvcli.py

## Explored AWS Lambda

```python
def lambda_handler(event, context):
    if event["name"] == "Marco":
        return "Polo"
    return "No!"
```

### Use Boto3

* install `boto3` and use `ipython`

### Build a computer vision cli

### Build a trigger that automatically runs a Lambda Function

```python
import boto3
from urllib.parse import unquote_plus

def label_function(bucket, name):
    """This takes an S3 bucket and a image name!"""
    print(f"This is the bucketname {bucket} !")
    print(f"This is the imagename {name} !")
    rekognition = boto3.client("rekognition")
    response = rekognition.detect_labels(
        Image={"S3Object": {"Bucket": bucket, "Name": name,}},
    )
    labels = response["Labels"]
    print(f"I found these labels {labels}")
    return labels


def lambda_handler(event, context):
    """This is a computer vision lambda handler"""

    print(f"This is my S3 event {event}")
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        print(f"This is my bucket {bucket}")
        key = unquote_plus(record['s3']['object']['key'])
        print(f"This is my key {key}")
        
    my_labels = label_function(bucket=bucket, 
        name=key)
    return my_labels
```










