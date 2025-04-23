FROM python:3.9-alpine

COPY ./requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY main.py /

ENV DAYS ""

CMD ["python3", "main.py"]