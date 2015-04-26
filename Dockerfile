FROM python:3-onbuild

RUN pip install uWSGI

CMD ["uwsgi", "--ini", "uwsgi.ini"]
