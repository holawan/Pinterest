FROM python:3.9.13

WORKDIR /home/

RUN echo "testing_image5"

RUN git clone https://github.com/holawan/Pinterest.git

WORKDIR /home/Pinterest/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient



EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pragmatic.settings.deploy && python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]