FROM python:3.7

RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

RUN pip install gunicorn django-environ gevent django psycopg2 psycopg2-binary

COPY . /opt/services/djangoapp/src

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "api.wsgi:application"]