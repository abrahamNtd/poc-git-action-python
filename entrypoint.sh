#!/bin/sh -l

echo "The arguments are: number 1: $1  number 2:  $2"
time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT