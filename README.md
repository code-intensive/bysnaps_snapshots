# BySnaps Snapshots

The BySnaps snapshots service.

## Poetry

This project uses poetry. It's a modern dependency management
tool.

To run the project use this set of commands:

```bash
poetry install
poetry run python -m snapshots
```

This will start the server on the configured host.

You can find swagger documentation at `/api/v1/docs`.

You can read more about poetry here: https://python-poetry.org/

## Docker

You can start the project with docker using this command:

```bash
docker compose -f docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f docker/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml --project-directory . up
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker compose -f docker-compose.yml --project-directory . build
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variabels should start with "SNAPSHOTS_" prefix.

For example if you see in your "snapshots/settings.py" a variable named like
`random_parameter`, you should provide the "SNAPSHOTS_RANDOM_PARAMETER"
variable to configure the value. This behaviour can be changed by overriding `env_prefix` property
in `snapshots.settings.Settings.Config`.

An exmaple of .env file (You can find it in the root project directory's .env.example):
```bash
DEBUG = boolean # false
ALLOWED_HOSTS = string # 127.0.0.1, 192.168.64.3 (comma separated)
SETTINGS_MODULE = string # 'config.settings'
SECRET_KEY = string
TOKEN_KEY = string

CLOUD_NAME = string
CLOUD_API_KEY = string
CLOUD_API_SECRET = string
CLOUD_URL= string

DB_PORT = integer # 5432
DB_PASSWORD = string # my*awesome^password
DB_USER = string # postgres
DB_HOST = string # localhost
DB_NAME = string # with slash prepended to it e.g /test_database
DB_DRIVERNAME = string # postgres
DB_ECHO = boolean # false
DB_SCHEME = string #postgresql+asyncpg
```

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possibe bugs);


You can read more about pre-commit here: https://pre-commit.com/

## Migrations

If you want to migrate your database, you should run following commands:
```bash
# To run all migrations untill the migration with revision_id.
alembic upgrade "<revision_id>"

# To perform all pending migrations.
alembic upgrade "head"
```

### Reverting migrations

If you want to revert migrations, you should run:
```bash
# revert all migrations up to: revision_id.
alembic downgrade <revision_id>

# Revert everything.
 alembic downgrade base
```

### Migration generation

To generate migrations you should run:
```bash
# For automatic change detection.
alembic revision --autogenerate

# For empty file generation.
alembic revision
```


## Running tests

If you want to run it in docker, simply run:

```bash
docker compose -f docker/docker-compose.yml --project-directory . run --rm api pytest -vv .
docker compose -f docker/docker-compose.yml --project-directory . down
```

For running tests on your local machine.
1. you need to start a database.

I prefer doing it with docker:
```
docker run -p "5432:5432" -e "POSTGRES_PASSWORD=snapshots" -e "POSTGRES_USER=snapshots" -e "POSTGRES_DB=snapshots" postgres:13.8-bullseye
```


2. Run the pytest.
```bash
pytest -vv .
```
