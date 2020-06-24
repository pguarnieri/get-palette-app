#!/bin/sh -x

cp -r get_palette ./packages/

pip3 install --target ./packages -r requirements/prod.txt
find ./packages -iname tests -type d -exec rm -rf {} +

cd ./packages
zip -r9 ${OLDPWD}/function.zip .

cd $OLDPWD
zip function.zip lambda_function.py