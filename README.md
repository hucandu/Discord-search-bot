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
REDIS_URL=redis://redis:6379/0
# REDIS_URL=redis://localhost:6379/0

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

Start Server
```sh
$(venv) python manage.py runserver 0.0.0.0:8000
```

### Using Docker

Build Image
```sh
$ docker-compose -f docker-compose.dev.yml build
```

Run container
```sh
$ docker-compose -f docker-compose.dev.yml up -d
$ docker-compose logs -f servicename
```

### Type checks

Running type checks with mypy:

```sh
$ mypy discord_search_bot
```

### Test coverage
To run the tests, check your test coverage, and generate an HTML coverage report::
```sh
$ coverage run -m pytest
$ coverage html
$ open htmlcov/index.html
```
To check the report in console:
```sh
$ coverage report -m
```

### Running tests with pytest
Use [pytest-django](https://pytest-django.readthedocs.io/en/latest/index.html) to write your test cases
```sh
$ pytest
```
