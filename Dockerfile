FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python3 -m pip install --upgrade pip

COPY requirements.txt /usr/app/

WORKDIR /usr/app/
RUN pip3 install -r requirements.txt && pip3 install pygments

COPY . /usr/app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#https://www.section.io/engineering-education/django-docker/