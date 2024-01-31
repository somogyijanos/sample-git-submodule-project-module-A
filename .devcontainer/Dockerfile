FROM python:3.12-slim

RUN apt-get update && apt-get install -y git tree

COPY pip-requirements.txt .
RUN pip install -r pip-requirements.txt
RUN rm pip-requirements.txt