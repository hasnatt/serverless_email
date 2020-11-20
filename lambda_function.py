import json
import smtplib
import config
from email.message import EmailMessage
import imghdr

EMAIL_ADDRESS = config.EMAIL_ADDRESS
EMAIL_PASSWORD = config.EMAIL_PASSWORD


msg = EmailMessage()
msg['Subject'] = 'test email 1'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'hsntbdl@gmail.com'
msg.set_content('fkgndfkgn knjfdkgfd')

with open('clouds.gif', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)    

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)



# def lambda_handler(event, context):
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')}

# if __name__ == "__main__":
#     event ={}
#     context = []
#     print(lambda_handler(event, context))