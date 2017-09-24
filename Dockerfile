FROM python:3.6-onbuild

RUN pip install uWSGI

CMD ["uwsgi", "--ini", "uwsgi.ini"]
