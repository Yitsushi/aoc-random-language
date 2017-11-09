#!/bin/bash

zip today-endpoint.zip language-pool.py

aws lambda update-function-code \
  --function-name AoC2017 \
  --zip-file fileb://today-endpoint.zip \
  --region us-east-1

rm today-endpoint.zip
