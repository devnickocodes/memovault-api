release: python manage.py makemigrations && python manage.py migrate
web: gunicorn memovault_api.wsgi