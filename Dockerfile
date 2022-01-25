FROM python:latest

WORKDIR /code

COPY requir.txt /code/

RUN pip install -U pip
RUN pip install -r requir.txt

COPY . /code/

EXPOSE 8000

CMD ["gunicorn", 'config.wsgi', ':8000']
