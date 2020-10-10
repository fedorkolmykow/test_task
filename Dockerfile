FROM python:3.7-alpine

ADD . .

RUN pip3 install -r requirements.txt
CMD [ "python3", "/main.py" ]