FROM python:3.8.6-slim as base

FROM base as builder

WORKDIR /install

RUN apt-get update \
    && pip install pipenv


COPY requirements.txt .
RUN pip install --prefix=/install --ignore-installed -r requirements.txt


FROM python:3.8.6-slim

ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /home
COPY . /home

COPY --from=builder /install /usr/local

RUN sed -i -e 's/\r$//' /home/startup.sh
RUN chmod +x /home/startup.sh
ENTRYPOINT /home/startup.sh