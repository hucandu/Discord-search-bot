# Discord Search BOT
A discord bot that searches text in google and returns respose

## Deployment
Deployment steps are mentioned in [DEPLOYMENT.md](DEPLOYMENT.md)

## Development

Some helper commands only for development machine
[django-extensions](https://django-extensions.readthedocs.io/en/latest/command_extensions.html)

Create environment configuration

Put the following in `.env` file
```dotenv

DATABASE_URL=mysql://root:root@mysql/discord_search_bot
# DATABASE_URL=mysql://user:password@localhost:3306/dbname
```


### Using virtualenv
Make sure `python3.7 -V` is installed
```sh
$ pip3 install virtualenv
$ virtualenv -p python3.7 venv
$ source ./venv/bin/activate
```

Install Dependencies
```sh
$(venv) pip install -r requirements/local.txt
```

Start Script
```sh
$(venv) python manage.py start_connection
```

### Using Docker

Build Image
```sh
$ docker-compose build
```

Run container
```sh
$ docker-compose run --rm django python manage.py start_connection
```

### Type checks

Running type checks with mypy:

```sh
$ mypy discord_search_bot
```
