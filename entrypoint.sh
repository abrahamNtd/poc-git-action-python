#!/bin/sh -l

echo "the arguments are: number 1: $1  number 2:  $2"
time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT