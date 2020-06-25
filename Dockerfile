FROM lambci/lambda:build-python3.7

ENV AWS_DEFAULT_REGION eu-west-2

COPY requirements requirements
RUN pip install -t ./packages -r requirements/prod.txt
RUN find ./packages -iname tests -type d -exec rm -rf {} +

RUN zip -9yr lambda.zip ./packages

COPY lambda_function.py .
COPY get_palette get_palette

RUN zip -9yr lambda.zip ./lambda_function.py
RUN zip -9yr lambda.zip ./get_palette

CMD aws lambda update-function-code --function-name myFunctionName --zip-file fileb://lambda.zip --debug --cli-connect-timeout 6000 2>&1 | grep -v ZipFile | grep -v "Unpacked value of"
