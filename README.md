```
# create artifact
$ zip today-endpoint.zip language-pool.py

# Upload artifact
$ aws s3 cp today-endpoint.zip s3://advent-of-code-2017/

# create stack
# ./create-stack.sh stack-name artifact-s3-bucket
$ ./create-stack.sh aoc2017 advent-of-code-2017
```
