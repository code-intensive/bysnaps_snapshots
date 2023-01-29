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
docker-compose -f deploy/docker/compose/snapshots/docker-compose.yml up --build
```

If you want to develop in docker with autoreload add update your .env file like this:

```env
SNAPSHOTS_RELOAD = true
```

This command exposes the web application on port 0.0.0.0, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f deploy/docker/compose/snapshots/docker-compose.yml build
```

## Project structure

```bash
$ tree "snapshots"
snapshots
.
├── .github
│   └── workflows
│       └── tests.yml
├── deploy
│   ├── docker
│   │   ├── compose
│   │   │   └── snapshots
│   │   │       └── docker-compose.yml
│   │   └── dockerfiles
│   │       └── snapshots
│   │           └── Dockerfile
│   └── kubernetes
│       └── .gitkeep
├── docs
│   └── .gitkeep
├── logs
│   └── pytest-logs.txt
├── snapshots
│   ├── api
│   │   ├── controllers
│   │   │   └── snap_controllers.py
│   │   ├── routes
│   │   │   └── api
│   │   │       └── snap_routes.py
│   │   └── services
│   │       ├── cloudinary
│   │       │   └── cloudinary_service.py
│   │       ├── decoders
│   │       │   └── cv2_decoder_service.py
│   │       ├── generators
│   │       │   └── qrcode_service.py
│   │       └── snaps
│   │           └── snaps_service.py
│   ├── config
│   │   ├── lifetimes
│   │   │   └── .gitkeep
│   │   ├── log_config.py
│   │   └── settings.py
│   ├── database
│   │   ├── config
│   │   │   └── setup.py
│   │   ├── managers
│   │   │   └── snap_manager.py
│   │   ├── migrations
│   │   │   ├── versions
│   │   │   ├── env.py
│   │   │   ├── README
│   │   │   └── script.py.mako
│   │   ├── models
│   │   │   └── models.py
│   │   └── utils
│   │       ├── model_converter.py
│   │       └── prebuilt_queries.py
│   ├── dependencies
│   │   └── service_dependency.py
│   ├── middlewares
│   │   └── cors_middleware.py
│   ├── models
│   │   └── pydantic
│   │       ├── snap_item.py
│   │       └── snaps.py
│   ├── protocols
│   │   ├── cloudinary
│   │   │   └── cloud_snap.py
│   │   ├── decoders
│   │   │   └── snap_decoder.py
│   │   ├── generators
│   │   │   └── snap_generator.py
│   │   ├── managers
│   │   │   └── manager.py
│   │   └── snaps
│   │       └── snap_service.py
│   ├── resources
│   │   ├── css
│   │   │   └── swagger-ui.css
│   │   └── js
│   │       ├── redoc.standalone.js
│   │       └── swagger-ui-bundle.js
│   ├── tests
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── test_create_snap.py
│   │   ├── test_delete_snap.py
│   │   ├── test_get_snap.py
│   │   ├── test_get_snaps.py
│   │   ├── test_health.py
│   │   └── test_update_snap.py
│   ├── utils
│   │   ├── id_generator.py
│   │   └── parsers.py
│   ├── __init__.py
│   ├── __main__.py
│   └── main.py
├── .dockerignore
├── .DS_Store
├── .editorconfig
├── .env
├── .env.example
├── .flake8
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── alembic.ini
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

Refer to the `.env.example` file for available environment variable configurations

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
* autoflake (removes unused imports);
* pytest (runs all test cases automatically).


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
docker compose -f deploy/docker/compose/snapshots/docker-compose.yml run --rm api pytest -vv .
docker compose -f deploy/docker/compose/snapshots/docker-compose.yml down
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
