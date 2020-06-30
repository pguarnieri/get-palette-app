#!/bin/sh -x

curl -v -X POST \
  'https://nqj2xhn207.execute-api.eu-west-2.amazonaws.com/beta/get-palette' \
  -H 'content-type: application/json' \
  -d @./tests/request.json \
  -o ./tests/output.json