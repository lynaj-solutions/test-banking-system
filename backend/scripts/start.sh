#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py migrate
# python ./manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root@example.com', 'root')"
python manage.py collectstatic --noinput --verbosity 0
python manage.py runserver_plus 0.0.0.0:8000

# lt$1ksd(djJ!3