FROM python:latest

COPY . .

RUN pip3 install -r requirements.txt
RUN python3 functionproj/manage.py makemigrations
RUN python3 functionproj/manage.py migrate

CMD [ "python3","functionproj/manage.py","runserver","0.0.0.0:8000"]