FROM python:3.9-alpine

COPY ./get_userid_accesskey.py /

ENV DAYS ""

CMD ["python3", "get_userid_accesskey.py"]