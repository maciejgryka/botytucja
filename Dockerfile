# this is basically kennethreitz/pipenv/, expanded for experimenting
FROM ubuntu:17.10

# -- Install Pipenv:
RUN apt update
RUN apt install software-properties-common python-software-properties python3-pip -y
RUN add-apt-repository ppa:pypa/ppa -y
RUN apt update
RUN apt install pipenv -y

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# -- Install Application into container:
RUN set -ex && mkdir /app

WORKDIR /app

# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

ENV TZ Europe/Berlin

# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system

COPY . /app

RUN useradd -m botytucja
USER botytucja
CMD python3 clock.py --access-logfile - --error-logfile - --log-file - --log-level info
