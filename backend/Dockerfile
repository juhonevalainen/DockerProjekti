FROM python:3.14.0a3-alpine3.21
WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install Flask && pip install flask-cors
EXPOSE 5000
ENTRYPOINT ["flask", "--app", "server", "run", "--host=0.0.0.0"]
