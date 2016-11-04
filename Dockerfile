FROM ubuntu:16.04
MAINTAINER Alan Sanchez <alan.sanchez@alumnos.udg.mx>

ENV DEBIAN_FRONTEND noninteractive
ENV MYSQLTMPROOT temprootpass

#Add keys [mongodb and mariadb]
RUN apt-get update && apt-get install -y software-properties-common \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 \
    && echo 'deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse' | tee /etc/apt/sources.list.d/mongodb-org-3.2.list \
    && apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8 \
    && add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://ftp.utexas.edu/mariadb/repo/10.1/ubuntu xenial main' \
    && apt-get update

#Install dependencies
RUN apt-get install -y \
    python-pip python-dev uwsgi-plugin-python \
    supervisor nodejs-legacy git npm \
    && npm install -g bower

#Install mongodb
RUN apt-get install -y mongodb-org \
    && mkdir -p /data/db

#Install nginx
RUN apt-get install -y nginx

#Install mariadb
# RUN echo mariadb-server-10.0 mysql-server/root_password password $MYSQLTMPROOT | debconf-set-selections; \
#     echo mariadb-server-10.0 mysql-server/root_password_again password $MYSQLTMPROOT | debconf-set-selections; \
RUN apt-get install -y mariadb-server

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
