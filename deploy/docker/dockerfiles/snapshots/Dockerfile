FROM python:3.10.8-slim-buster

ARG WORKDIR

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && apt-get install -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

# Install dependency manager
RUN pip install poetry==1.2.2

# Configuring poetry
RUN poetry config virtualenvs.create false

# Copying project dependencies and config
COPY poetry.lock pyproject.toml /app/src/

# Set working directory to /app/src/
WORKDIR /app/src

# Removing gcc
RUN apt-get purge -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

# Copying actual application
COPY . /app/src

# Installing requirements
RUN poetry install --no-interaction --no-ansi

CMD ["/usr/local/bin/python", "-m", "snapshots"]
