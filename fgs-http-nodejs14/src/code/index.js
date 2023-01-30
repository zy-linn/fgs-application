exports.handler = async (event, context) => {
    console.log('process request from apig trigger');

    let responseType = 'default';
    if(event.queryStringParameters && event.queryStringParameters.responseType){
        responseType = event.queryStringParameters.responseType;
    }

    let output = '';
    if(responseType === 'html'){
        output = {
            'statusCode': 200,
            'isBase64Encoded': false,
            'headers': {
                'Content-type': 'text/html; charset=utf-8'
            },
            'body': '<html><h1>Welcome to use FunctionGraph</h1></html>'
        };
    } else if(responseType === 'json'){
        output = {
            'statusCode': 200,
            'isBase64Encoded': false,
            'headers': {
                'Content-type': 'application/json'
            },
            'body': '{"key": "value"}'
        };
    } else {
        output = {
            'statusCode': 200,
            'isBase64Encoded': false,
            'headers': {
                'Content-type': 'text/html; charset=utf-8'
            },
            'body': '<html>Please construct the url with query parameters responseType=html, responseType=json</html>'
        };
    }
    return output;
}
