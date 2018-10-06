#!/bin/bash

name="${1:-AoC2018}"

zip today-endpoint.zip language-pool.py

aws lambda update-function-code \
  --function-name "${name}" \
  --zip-file fileb://today-endpoint.zip \
  --region us-east-1

rm today-endpoint.zip
