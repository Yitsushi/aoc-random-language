#!/bin/bash

name="${1:-AoC2018}"
aws_account="${2:-123456789}"

zip today-endpoint.zip language-pool.py

aws lambda create-function \
  --region us-east-1 \
  --function-name "${name}" \
  --zip-file fileb://today-endpoint.zip \
  --role arn:aws:iam::${aws_account}:role/lambda_basic_execution \
  --handler language-pool.index \
  --runtime python2.7 \
  --timeout 15 \
  --memory-size 512

rm today-endpoint.zip
