FROM python:3.6.2
# this will fail, set with other values when running live
ENV GITHUB_TOKEN=abcdef123

COPY start.sh /scripts/start.sh
COPY app /app
COPY requirements.txt /

RUN ls -al /app

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
RUN chmod +x /scripts/*.sh

WORKDIR /app

ENTRYPOINT ["/scripts/start.sh"]