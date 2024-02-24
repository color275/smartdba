FROM python:3.8
ENV PYTHONUNBUFFERED 1
ADD . /smartdba
WORKDIR /smartdba
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
