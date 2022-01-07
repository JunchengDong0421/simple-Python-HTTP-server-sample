sudo gunicorn -c gunicorn_conf.py app:app &
# Replace the default config file (/usr/local/nginx/conf/nginx.conf) with the one in folder first!
sudo nginx