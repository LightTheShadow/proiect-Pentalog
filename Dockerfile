FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir Flask pytest

COPY src ./

EXPOSE 5000 

CMD [ "python", "./flask_entrypoint.py" ]
