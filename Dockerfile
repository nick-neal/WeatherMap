FROM python:3.10-slim-bullseye

RUN mkdir /app
ADD ./app /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000

#Run App
CMD ["python3","app.py"]