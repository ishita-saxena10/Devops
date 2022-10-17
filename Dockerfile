FROM python:latest



WORKDIR /usr/app/src


COPY unit_test.py ./




CMD [ "python", "./unit_test.py"]