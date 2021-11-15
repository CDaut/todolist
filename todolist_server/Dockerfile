FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir /todolist_server
WORKDIR /todolist_server
ADD ./requirements.txt /todolist_server/
RUN pip3 install -r requirements.txt
ADD ./ /todolist_server/
