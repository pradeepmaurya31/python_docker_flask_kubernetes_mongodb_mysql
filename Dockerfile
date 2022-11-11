FROM python:3.10

RUN apt-get -y update   && apt-get install -y --no-install-recommends --no-install-suggests default-libmysqlclient-dev && pip install --no-cache-dir --upgrade pip

WORKDIR /pfdk9

COPY ./requirements.txt /pfdk9

RUN pip install --no-cache-dir --requirement /pfdk9/requirements.txt 

COPY . /pfdk9

EXPOSE 5000

CMD ["python3", "server.py"]



