import json
import smtplib
import config
from email.message import EmailMessage
import imghdr
import os 

EMAIL_ADDRESS = config.EMAIL_ADDRESS
EMAIL_PASSWORD = config.EMAIL_PASSWORD


msg = EmailMessage()
msg['Subject'] = 'test email 1'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'hsntbdl@gmail.com'
msg.set_content('fkgndfkgn knjfdkgfd')

attatchment_files = list()
for root, dirs, files in os.walk("attatchments/"):
    for filename in files:
        attatchment_files.append(filename)

for file in attatchment_files:
    

    path = './attatchments/' + str(file)
    print(path)
    with open(path, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.path)
        file_name = f.path


    # msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)    

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(msg)



# def lambda_handler(event, context):
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')}

# if __name__ == "__main__":
#     event ={}
#     context = []
#     print(lambda_handler(event, context))