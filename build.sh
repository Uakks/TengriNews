#!/bin/bash

python manage.py migrate &&
python manage.py parsing &&
python manage.py import_json