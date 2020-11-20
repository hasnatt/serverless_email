import json

def lambda_handler(event, context):

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }



if __name__ == "__main__":

    event ={

    }
    context = []
    print(lambda_handler(event, context))