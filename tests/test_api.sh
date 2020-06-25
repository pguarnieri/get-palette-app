#!/bin/sh -x

curl -v -X POST \
  'https://avx8addboa.execute-api.eu-west-2.amazonaws.com/beta/get-palette' \
  -H 'content-type: application/json' \
  -d ./tests/request.json \
  -o ./tests/output.json