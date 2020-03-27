# Deployment

### Create log directory

```sh
$ mkdir -p /var/log/app/discord_search_bot/ && chmod -R 777 /var/log/app/discord_search_bot/
```

### Create environment configuration

Put the following in `.env` file

```dotenv
DJANGO_SETTINGS_MODULE=config.settings.production

DJANGO_SECRET_KEY=<random_generated_key>
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_SECURE_SSL_REDIRECT=False
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=False
DJANGO_SECURE_HSTS_PRELOAD=False
DJANGO_SECURE_CONTENT_TYPE_NOSNIFF=False
DATABASE_URL=mysql://user:password@localhost:3306/dbname

# Redis Config
REDIS_URL=redis://<redis_host>:6379/<database>
```

You can create random key for django using:
```sh
python -c 'import random; result = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]); print(result)'
```

### Clone the project

Try to clone in some standard location. DO NOT CLONE in `/var/www/html`

Deploy in `/var/app/python/discord_search_bot/` directory.

```sh
$ git clone https://gitlab.com/hucandu@gmail.com/discord_search_bot.git .
```

### Install Dependencies

Use pip3 or pip for python3 only

```sh
$ pip3 install -r requirements/production.txt
```

### Verify Django Setup

Start a simple server
```sh
$ python3 manage.py runserver 0.0.0.0:9000
```

and verify with
```sh
curl -XPOST http://localhost:9000
```

This should make your basic setup working.

## Server Setup

### Install gunicorn3

```sh 
apt-get install -y gunicorn3
```

### Setup Supervisor service configuration

Paste the following contents in `/etc/supervisor/conf.d/discord_search_bot.conf`

```ini
[program:discord_search_bot]
command=gunicorn3 -b="127.0.0.1:9000" -w 3 --forwarded-allow-ips="localhost" --access-logfile /var/log/app/discord_search_bot/access.log --error-logfile /var/log/app/discord_search_bot/error.log --log-level debug config.wsgi
directory=/var/app/python/discord_search_bot/
user=root
autostart=true
autorestart=true
redirect_stderr=true
```

and start supervisor
```sh
/etc/init.d/supervisor restart
``` 

### Setup Reverse proxy to supervisor

#### Using Nginx

```nginx
  upstream discord_search_bot {
     server localhost:9000 fail_timeout=0;
  }

 server {
    listen 80;
    client_max_body_size 4G;

    server_name discordsearchbot.tk;

    keepalive_timeout 5;

    # path for static files
    location / {
      try_files $uri @proxy_to_app;
    }

    location ~ /\. {
        deny all;
        access_log off;
        log_not_found off;
    }


    location @proxy_to_app {
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
      proxy_set_header Host localhost;
      proxy_redirect off;
      proxy_pass http://discord_search_bot;

    }

    error_page 500 502 503 504 /500.html;
    access_log /var/log/nginx/discord_search_bot.access.log combined;
    error_log  /var/log/nginx/discord_search_bot.error.log warn;

    location = /500.html {
      root /path/to/app/current/public;
    }
}
```
