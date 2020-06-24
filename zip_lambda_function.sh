#!/bin/sh -x

cp -r get_palette ./packages/

pip3 install --target ./packages -r requirements/prod.txt
rm -rf ./packages/**/tests

cd ./packages
zip -r9 ${OLDPWD}/function.zip .

cd $OLDPWD
zip function.zip lambda_function.py