FROM ubuntu:16.04
MAINTAINER Alan Sanchez <alan.sanchez@alumnos.udg.mx>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 \
    && echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list \
    && apt-get update && apt-get install -y \
    python-pip python-dev uwsgi-plugin-python \
    nginx supervisor nodejs-legacy git npm \
    mongodb-org \
    && npm install -g bower \
    && mkdir -p /data/db
COPY flask.conf /etc/nginx/sites-available/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY . /var/www/app

RUN mkdir -p /var/log/nginx/app /var/log/uwsgi/app /var/log/supervisor \
    && rm /etc/nginx/sites-enabled/default \
    && ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf \
    && echo "daemon off;" >> /etc/nginx/nginx.conf \
    && pip install -r /var/www/app/requirements.txt \
    && chown -R www-data:www-data /var/www/app \
    && chown -R www-data:www-data /var/log \
    && cd /var/www/app \
    && npm install \
    && bower install --allow-root

CMD ["/usr/bin/supervisord"]
