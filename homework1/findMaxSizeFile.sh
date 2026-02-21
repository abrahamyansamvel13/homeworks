#!/bin/bash 

find . -type f -exec du -h {} + | sort -hr | head -n 1

#find . -type  to finde all files
#du -h for size
# sort -hr sort from max to min
#head -n 1  display max size file


