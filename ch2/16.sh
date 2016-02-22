#!/bin/bash

if [ $# -lt 2 ]; then
  echo "Error: please input number and filneame to split";
  exit 1
fi

line_num=`wc -l $2`
num=`expr $1 / $line_num`
split -l $num $2
