FROM python:3.10-slim

ENV APP_HOME /
WORKDIR $APP_HOME

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt


ENTRYPOINT ["python", "app/run.py"]


