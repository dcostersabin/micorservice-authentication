python3 manage.py migrate;
python3 manage.py collectstatic;
uwsgi --http :8002 --wsgi-file /opt/service-2/core/wsgi.py;
