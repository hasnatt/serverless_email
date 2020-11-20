import json
import smtplib
import config

EMAIL_ADDRESS = config.EMAIL_ADDRESS
EMAIL_PASSWORD = config.EMAIL_PASSWORD

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    # encrypt with tls
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Test email'
    body = 'fkgndfkgn knjfdkgfd'
    message = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'hsntbdl@gmail.com', message)

# def lambda_handler(event, context):

#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }



# if __name__ == "__main__":

#     event ={

#     }
#     context = []
#     print(lambda_handler(event, context))