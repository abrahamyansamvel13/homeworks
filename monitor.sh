#!/bin/bash

df -P / | awk 'NR==2 {print 100 - substr($5, 1, length($5)-1) "%"}'

