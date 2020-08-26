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







