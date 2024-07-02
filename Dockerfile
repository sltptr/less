FROM python:3.12-slim

WORKDIR /src

RUN apt-get update && apt-get install -y cron && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY src/requirements.txt .
RUN python -m venv .venv && \
    . .venv/bin/activate && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY src/crontab /etc/cron.d/app-crontab
RUN chmod 0644 /etc/cron.d/app-crontab && crontab /etc/cron.d/app-crontab && touch /var/log/cron.log

COPY src/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY src .
RUN chmod +x /src/loadenv.sh


EXPOSE 5000

ENTRYPOINT ["/entrypoint.sh"]

