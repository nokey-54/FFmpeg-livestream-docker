FROM python:3.9
RUN  pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN chmod -R 777 /app
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg
RUN pip install --upgrade -r /app/requirements.txt
COPY . /app
CMD ["python", "stream.py"]