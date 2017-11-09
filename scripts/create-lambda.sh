#!/bin/bash

zip today-endpoint.zip language-pool.py

aws lambda create-function \
  --region us-east-1 \
  --function-name AoC2017 \
  --zip-file fileb://today-endpoint.zip \
  --role arn:aws:iam::659712256974:role/lambda_basic_execution \
  --handler language-pool.index \
  --runtime python2.7 \
  --timeout 15 \
  --memory-size 512

rm today-endpoint.zip
