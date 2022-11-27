FROM python:3.10.8-slim-buster

RUN apt-get update && apt-get install -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

# Install dependency manager
RUN pip install poetry==1.2.2

# Configuring poetry
RUN poetry config virtualenvs.create false

# Copying project dependencies and config
COPY poetry.lock pyproject.toml /app/src/

# Set to working directory to /app/src/
WORKDIR /app/src

# Installing requirements
RUN poetry install

# Removing gcc
RUN apt-get purge -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

# Copying actual application
COPY . /app/src
RUN poetry install

CMD ["/usr/local/bin/python", "-m", "snapshots"]
