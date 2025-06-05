# pull official base image
FROM python:3.11.3-slim-buster

# set work directory
WORKDIR /usr/src/app/server

# set environment variables
ENV FLASK_ENV=dev
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc supervisor && \
    rm -rf /var/lib/apt/lists/*

# copy supervisor config
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# upgrade pip
RUN pip install --upgrade pip

# install Python dependencies
COPY ./requirements.txt /usr/src/app/server/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# expose port 5000 for Flask app
EXPOSE 5000

# copy application code
COPY . .

# run supervisord to start processes
CMD ["supervisord"]
