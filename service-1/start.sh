python3 manage.py migrate;
python3 manage.py collectstatic;
uwsgi --http :8001 --wsgi-file /opt/service-1/core/wsgi.py;
