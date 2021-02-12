#!/bin/bash

# Create local environment
python3 -m venv .env

ln -s $(pwd)/scripts .env/lib/python3.*/site-packages/