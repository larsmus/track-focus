#!/usr/bin/env bash

git pull
python3 focus.py
open focused_plot.html
git add .
git commit -m "update data"
git push origin master

