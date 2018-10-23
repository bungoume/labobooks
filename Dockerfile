FROM python:3.7.1-onbuild

RUN pip install uWSGI

CMD ["uwsgi", "--ini", "uwsgi.ini"]
