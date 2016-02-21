#!/bin/bash

if [ $# -lt 2 ]; then
  echo "Error: please specify number and filename"
  exit 1
fi

head -n $1 $2
