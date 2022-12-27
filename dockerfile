# For production
FROM python:3.7-slim-buster
RUN apt-get update && apt update && apt upgrade -y
RUN apt-get install -y \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python-all-dev \
    libsm6 \
    libxext6 \
    libxrender-dev
RUN apt install -y python-opencv

COPY . .

ENV PYTHONUNBUFFERED True
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8080
ENTRYPOINT ["python3", "main.py"]


# # For development
# FROM ishansingla/webrtc:latest

# ADD . .

# EXPOSE 8080
# ENTRYPOINT ["python", "main.py"]