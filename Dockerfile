FROM ubuntu:latest

WORKDIR /pa
RUN apt-get update && apt-get install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD [ "python3","main.py" ]
