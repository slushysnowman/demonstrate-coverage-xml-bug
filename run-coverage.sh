#!/bin/bash
coverage run --source scripts -m unittest discover -s tests
coverage report
coverage xml