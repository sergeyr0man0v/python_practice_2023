#!/bin/bash

python3 -m venv venv
pip install virtulenv
virtulenv venv
source venv/bin/activate

pip install -r requirements.txt

python3 main.py
