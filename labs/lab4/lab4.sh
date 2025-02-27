#!/bin/bash

FILE=$1
BUCKET=$2
LENGTH=$3

aws s3 cp $FILE s3://$BUCKET/
url=$(aws s3 presign --expires-in $LENGTH s3://$BUCKET/$FILE)
echo $url

