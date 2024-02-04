FROM library/python:3.10-slim-buster

RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # psycopg2 dependencies
    && apt-get install -y libpq-dev \
    # Translations dependencies
    && apt-get install -y gettext \
    && apt-get install -y libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN useradd ubuntu --create-home -m -s /bin/bash

RUN mkdir -p /home/ubuntu/app
WORKDIR /home/ubuntu/app

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt 

COPY . /home/ubuntu/app
RUN python -m pytailwindcss -i static/src/main.css -o static/src/output.css

RUN chown -R ubuntu:ubuntu /home/ubuntu/app

USER ubuntu
ENV DJANGO_SETTINGS_MODULE="config.settings.production"
EXPOSE 80

CMD ["sh", "./runserver.sh"]
