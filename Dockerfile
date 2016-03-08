FROM python:3.5
MAINTAINER contato@gestaolivre.org
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
RUN mkdir -p /code
WORKDIR /code
ADD ./requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
CMD [ "python", "manage.py runserver" ]
