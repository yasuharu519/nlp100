#!/bin/bash

if [ $# -lt 1 ]; then
  echo "Error: Please specify input filename"
  exit 1
fi

wc -l $1
