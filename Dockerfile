FROM python:3.9

ADD . /zebtest
WORKDIR /zebtest
RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENV FLASK_APP=flask_app.py

CMD flask run --host=0.0.0.0 --port=5000

