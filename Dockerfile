FROM python:latest



WORKDIR /usr/app/src


COPY Calculator.py ./




CMD [ "python", "./Calculator.py"]