# handler.py

import numpy as np
import json


def main(event, context):

    # This is just for test the external packages
    a = np.arange(15).reshape(3, 5)
    print("Your numpy array:")
    print(a)

    # Here starts an example of how to handle a GET and POST params
    first_name = "nombre_base"
    last_name = "apellido_base"

    if event["httpMethod"] == "GET":
        try:
            first_name =  event["queryStringParameters"]["first_name"]
            last_name =  event["queryStringParameters"]["last_name"]
        except:
            first_name = "nombre_get_except"
            last_name = "apellido_get_except"
            

    if event["httpMethod"] == "POST":
        data = json.loads(event['body'])
        try:
            first_name = data["first_name"]
            last_name = data["last_name"]
        except:
            first_name = "nombre_post_except"
            last_name = "apellido_post_except"


    message = 'Hello {} {}!'.format(first_name, last_name)
    body = {
        "message": message
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response


# This is for local testing the code without lambda
if __name__ == "__main__":
    main('', '')

