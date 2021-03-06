import json
import smtplib
import config
import content
from email.message import EmailMessage
import imghdr
import os 
from jinja2 import Template

# macros
EMAIL_ADDRESS = config.EMAIL_ADDRESS
EMAIL_PASSWORD = config.EMAIL_PASSWORD
EMAIL_TO = config.EMAIL_TO
HTML_CONTENT = content.get_html()


def lambda_handler(event, context):
    # construct email
    msg = EmailMessage()
    msg['Subject'] = 'Daily Email'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_TO
    msg.set_content(HTML_CONTENT, subtype = 'html')

    # add attachments
    attachment_files = os.listdir('attachments/')
    for filename in attachment_files:
        file = os.path.join('attachments/', filename)
        with open(file, 'rb') as f:
            file_data = f.read()
            # file_type = imghdr.what(f.name)
            file_name =os.path.basename(f.name)
        # add attachment to the message
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)    

    # SMTP send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    return {
        'statusCode': 200,
        'body': json.dumps('email sent')}

# if __name__ == "__main__":
#     event ={}
#     context = []
#     print(lambda_handler(event, context))