[![Build Status](https://travis-ci.org/acidjunk/django-scrumboard.svg?branch=master)](https://travis-ci.org/acidjunk/django-scrumboard) [![Coverage Status](https://coveralls.io/repos/acidjunk/django-scrumboard/badge.svg?branch=master)](https://coveralls.io/r/acidjunk/django-scrumboard?branch=master)

A monolith implementation of a recruiting platform, focused on developers

Create a postgres DB and ensure that you user can create DB's

`$ python manage.py migrate`
python manage.py sitetrees
python manage.py createsuperuser
python manage.py runserver


Changelog
----------
*v0.1*
- added working DB model
- added license
- added tests
- added a design
- added Developer + Projects + Skill models, views and templates
- added social auth
- added static pages

Copyright (C) 2019 René Dohmen <acidjunk@gmail.com>
