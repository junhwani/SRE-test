FROM python:3.9-alpine

COPY ./requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./get_userid_accesskey.py /

ENV DAYS ""

CMD ["python3", "get_userid_accesskey.py"]