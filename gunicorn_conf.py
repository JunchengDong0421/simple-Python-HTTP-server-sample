debug = True

accesslog = "gunicorn_access.log"
loglevel = "debug"

workers = 5
worker_class = "gevent"
bind = "0.0.0.0:8080"
