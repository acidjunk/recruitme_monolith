[![Build Status](https://travis-ci.com/acidjunk/recruitme_monolith.svg?branch=master)](https://travis-ci.com/acidjunk/recruitme_monolith) [![Coverage Status](https://coveralls.io/repos/acidjunk/django-scrumboard/badge.svg?branch=master)](https://coveralls.io/r/acidjunk/django-scrumboard?branch=master)

A monolith implementation of a recruiting platform, focused on developers.

Mainly used to demonstrate some best practices regarding Django app structure and testing 
with Pytest fixtures. The src code is also used to facilitate a short py.test tutorial

Quickstart
----------

The database assumes you will be using postgres. Please ensure that your postgres user 
can create and drop DB's or has postgres superuser rights
```
createuser -s -P recruitme  # add ` -U postgres` if you are not a postgres superuser  
createdb recruitme
# Make a venv: this could be a different process/path on your workstation
mkvirtualenv --python=/usr/local/bin/python3 recruitme
pip install -r requirements.txt
pip install -r requirements_test.txt
```

For the tutorial/testing you can continue with a DB with some content
```
wget https://www.dropbox.com/s/fn5o5dqn7g0rftt/recruitme_monolith_tutorial.psql?dl=0
psql -d recruitme < recruitme_monolith_tutorial.psql
```

Or start from scratch with an empty DB:
```
python manage.py migrate
python manage.py sitetree_resync_apps
python manage.py createsuperuser
python manage.py runserver
```

Running tests:
```
$ py.test # or execute py.test from any sub folder in unit_tests/
$ pt.test -n auto
$ pytest --cov=recruitme
$ py.test PATH 
```

Changelog
---------
*v0.1*
- added working DB model
- added license
- added tests
- added a design
- added Developer + Projects + Skill models, views and templates
- added social auth
- added static pages

*v0.2*
- added tests
- upgraded semantic
- upgraded packages: project now works with python3.7
- added tutorial info and comments + DB to bootstrap your env


License
-------
Copyright (C) 2019 René Dohmen <acidjunk@gmail.com>

Licensed under the GNU GENERAL PUBLIC LICENSE Version 3
A copy of the LICENSE is included in the project.
