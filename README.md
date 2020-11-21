# AWS serverless email in Python
A boiler template for sending scheduled emails in AWS Lambda



deployment cli

virtualenv env

source env/bin/activate

pip install requests

pip install jinja2


deactivate


cd env/lib/python3.8/site-packages

zip -r my-deployment-package.zip .

mv my-deployment-package.zip ../../../../

cd ../../../../

zip -g my-deployment-package.zip lambda_function.py template.html content.py config.py attatchments    

aws lambda update-function-code --function-name send_email --zip-file fileb://my-deployment-package.zip