#!/bin/sh -x

pip3 install --target ./packages -r requirements.txt

cd ./packages
zip -r9 ${OLDPWD}/function.zip .

cd $OLDPWD
zip function.zip lambda_function.py

aws lambda update-function-code --function-name my-function --zip-file fileb://function.zip