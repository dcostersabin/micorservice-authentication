python3 manage.py migrate;
python3 manage.py collectstatic;
uwsgi --http :8000 --wsgi-file /opt/auth-service/core/wsgi.py;
