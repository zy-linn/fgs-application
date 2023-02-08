# -*- coding:utf-8 -*-
'''
The following is an APIG event of a sample function.
You can test this function by selecting the api-event-template event template.

{
  "httpMethod": "GET",
  "path": "/test/hello",
  "pathParameters": {
    "proxy": "hello"
  },
  "queryStringParameters": {
    "name": "me"
  },
  "headers": {
    "x-stage": "test",
    "Host": "wt6mne2s9k.execute-api.xxx.com",
    "User-Agent": "lua-resty-http/0.10 (Lua) ngx_lua/10008"
  },
  "body": "……",
  "requestContext": {
    "stage": "test",
    "requestId": "dd4337362c02c7d77299e78781beb4b1",
    "apiId": "41b45ea3-70b5-11e6-b7bd-69b5aaebc7d9"
  },
}
'''
import os
import json
import base64

def handler(event, context):
    print('process request from apig trigger')

    try:
        responseType = event['queryStringParameters']['responseType']
    except:
        responseType = 'default'

    if responseType == 'html':
        htmlResponse = {
            'statusCode': 200,
            'isBase64Encoded': True,
            'headers': {
                "Content-type": "text/html; charset=utf-8"
            },
            'body': base64.b64encode('<html><h1>Welcome to use FunctionGraph'
                    '</h1></html>'.encode(encoding="utf-8")).decode(),
        }
        return json.dumps(htmlResponse)

    elif responseType == 'json':
        jsonResponse = {
            'statusCode': 200,
            'isBase64Encoded': True,
            'headers': {
                "Content-type": "application/json"
            },
            'body': base64.b64encode('{"key": "value"}'.encode(encoding="utf-8")).decode(),
        }
        return json.dumps(jsonResponse)

    else:
        defaultResponse = {
            'statusCode': 200,
            'isBase64Encoded': True,
            'headers': {
                "Content-type": "text/html; charset=utf-8"
            },
            'body': base64.b64encode('<html>Please construct the url '
                    'with query parameters responseType=html, responseType='
                    'json</html>'.encode(encoding="utf-8")).decode(),
        }
        return json.dumps(defaultResponse)