![Python application test with Github Actions](https://github.com/noahgift/function-bike-rider/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg)

# function-bike-rider
This is a repo for showing what you can do with a function

You can watch a Video Walkthrough here:


[![The Power of Functions in Python](https://img.youtube.com/vi/lN6OSIDpgyg/0.jpg)](https://youtu.be/lN6OSIDpgyg)

## Building a CLI Workflow

1.  Create scaffolding in Python (Makefile, virtualenv)
2.  Write a function in a script file
3.  Test it out in IPython
4.  Write a test using pytest and test_hello.py
5.  Write a Click commandline tool
6.  Test all of it using the Click test runner


## Building a Computer Vision

1.  Create scaffolding in Python (Makefile, virtualenv)
2.  Write a function in a script file
3.  Test it out in IPython
4.  Write a test using pytest and test_hello.py
5.  Write a Click CLI tool
6.  Test all of it using the Click test runner
7.  Build an AWS Lambda function
8.  Create Trigger to S3 Bucket

## Building a Flask Application on GCP

1.  Create scaffolding in Python (Makefile, virtualenv)
2.  Write a function in a script file
3.  Test it out in IPython
4.  Write a test using pytest and test_hello.py
5.  Test out in Google Cloud Shell
6.  Deploy
7. `gcloud app create` 
8. `gcloud app deploy`
9. create `app.yaml`

## Build out a GCP Cloud Function

1.  Create scaffolding in Python (Makefile, virtualenv)
2.  Write a function in a script file
3.  Test it out in IPython
4.  Write a test using pytest and test_hello.py
5.  Test out in Google Cloud Shell
6.  Create Google Cloud Function  
7.  Invoke via the cli:
    `gcloud functions call ChangeMachineCloudFunction --data '{"amount":"11.44"}'`
```bash
executionId: akqyz3e60z6o
result: "This is the res: [{45: 'quarters'}, {1: 'dimes'}, {1: 'nickels'}, {4: 'pennies'}]"
```
8.  Another way to invoke is via curl command
To invoke via curl

```bash
curl -d '{
    "amount":"1.34"
}'     -H "Content-Type: application/json" -X POST <trigger>/function-3
```





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
### GCP Cloud Function that Translates

```python
import wikipedia

from google.cloud import translate

def sample_translate_text(text="YOUR_TEXT_TO_TRANSLATE", 
    project_id="YOUR_PROJECT_ID", language="fr"):
    """Translating Text."""

    client = translate.TranslationServiceClient()

    parent = client.location_path(project_id, "global")

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        parent=parent,
        contents=[text],
        mime_type="text/plain",  # mime types: text/plain, text/html
        source_language_code="en-US",
        target_language_code=language,
    )
    print(f"You passed in this language {language}")
    # Display the translation for each input text provided
    for translation in response.translations:
        print(u"Translated text: {}".format(translation.translated_text))
    return u"Translated text: {}".format(translation.translated_text)

def translate_test(request):
    """Takes JSON Payload {"entity": "google"}
    """
    request_json = request.get_json()
    print(f"This is my payload: {request_json}")
    if request_json and 'entity' in request_json:
        entity = request_json['entity']
        language = request_json['language']
        sentences = request_json['sentences']
        print(entity)
        res = wikipedia.summary(entity, sentences=sentences)
        trans=sample_translate_text(text=res, project_id="cloudai-194723",
            language=language )
        return trans
    else:
        return f'No Payload'
 ```

#### Example Output of GCP Cloud Function

Send payload in:
```
{
        "entity":"google",
        "language":"es",
        "sentences":"3"
}
```
The result below:

Translated text: Google LLC es una empresa de tecnología multinacional estadounidense que se especializa en servicios y productos relacionados con Internet, que incluyen tecnologías de publicidad en línea, un motor de búsqueda, computación en la nube, software y hardware. Se considera una de las cuatro grandes empresas de tecnología junto con Amazon, Apple y Microsoft. Google fue fundada en septiembre de 1998 por Larry Page y Sergey Brin mientras eran Ph.D. estudiantes de la Universidad de Stanford en California. Juntos poseen alrededor del 14 por ciento de sus acciones y controlan el 56 por ciento del poder de voto de los accionistas a través de acciones de supervotación.


Finally, you can call from the CLI:

```bash
gcloud functions call translate-wikipedia --data '{"entity":"google", "sentences
": "20", "language":"es"}'
```




