#!/bin/bash
source ~/.virtualenvs/recruitme/bin/activate
#export $(cat env | grep -v ^# | xargs)
python manage.py runserver
