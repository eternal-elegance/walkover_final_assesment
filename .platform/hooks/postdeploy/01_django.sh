#!/bin/bash

source /var/app/venv/*/bin/activate && {

# collecting static files
python manage.py collectstatic --noinput;
# log which migrations have already been applied
python manage.py showmigrations;
# migrate the rest
python manage.py migrate --noinput;
# another command to create a superuser (write your own)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('walkover', 'walkover@mail.com', 'walkover@1234')" | python manage.py shell

}