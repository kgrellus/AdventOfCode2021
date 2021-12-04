#!/usr/bin/env sh

DIR=$1
cd "./$DIR" || exit

python3 main.py
