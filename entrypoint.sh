#!/bin/sh -l

echo "the arguments are: $1 $2"
time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT