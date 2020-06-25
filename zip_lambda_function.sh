#!/bin/sh -x

cp -r get_palette ./packages

# pip3 install --target ./packages -r requirements/prod.txt

# rm -r ./packages/numpy
# rm -r ./packages/sklearn

unzip -o './lambda_wheels/*' -d ./packages

rm -r ./packages/*.dist-info ./packages/*/__pycache__
find ./packages -iname tests -type d -exec rm -rf {} +

cd ./packages
zip -r9 ${OLDPWD}/function.zip .

cd $OLDPWD
zip function.zip lambda_function.py