#!/bin/bash 

#find . -type f -exec du -h {} + | sort -hr | head -n 1

#find . -type  to finde all files
#du -h for size
# sort -hr sort from max to min
#head -n 1  display max size file

DIR="${1:-.}"

find "$DIR" \
  -type d \( -path /proc -o -path /sys -o -path /dev \) -prune -o \
  -type f -exec du -h {} + \
| sort -hr | head -n 1
