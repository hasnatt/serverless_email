import json
import smtplib
import config
import content
from email.message import EmailMessage
import imghdr
import os 

EMAIL_ADDRESS = config.EMAIL_ADDRESS
EMAIL_PASSWORD = config.EMAIL_PASSWORD
HTML_CONTENT = content.HTML_CONTENT


msg = EmailMessage()
msg['Subject'] = 'Images'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'hsntbdl@gmail.com'
# msg.set_content('Plain text email')

msg.set_content(HTML_CONTENT, subtype = 'html')


attatchment_files = os.listdir('attatchments/')

for filename in attatchment_files:
    file = os.path.join('attatchments/', filename)
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        print(file_type)
        file_name =os.path.basename(f.name)

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)    

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