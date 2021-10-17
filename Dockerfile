FROM python:3.9-alpine

ADD . /app

WORKDIR /app
RUN pip install -r requirements.txt

# 1時間
RUN echo '0 * * * * cd /app; python src/main.py' > /var/spool/cron/crontabs/root

ENTRYPOINT ["crond", "-f"]