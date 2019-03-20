#!/bin/bash
cd "$(dirname "$0")"
cd ..
python manage.py delete_sitetrees
python manage.py sitetree_resync_apps
