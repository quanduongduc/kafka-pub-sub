FROM python:3.10-slim-buster

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt clean && \
    rm -rf /var/cache/apt/*

RUN apt-get -y install inotify-tools
RUN apt-get -y install procps

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8




COPY requirements.txt /tmp/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /src
ENV PATH "$PATH:/src/scripts"
ENV PYTHONPATH "${PYTHONPATH}:/src/src"

RUN useradd -m -d /src -s /bin/bash app \
    && chown -R app:app /src/* && chmod +x /src/scripts/*

WORKDIR /src
USER app

CMD ["./scripts/start-mailer.sh", "&&", "./scripts/start-server.sh"]
