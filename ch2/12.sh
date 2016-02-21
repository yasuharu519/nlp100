#!/bin/bash

if [ $# -lt 1 ]; then
  echo "Error: Please specify filename"
  exit 1
fi

cut -d' ' -f 1 $1 > col1.txt
cut -d' ' -f 2 $1 > col2.txt
