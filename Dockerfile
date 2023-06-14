FROM python:3.9-slim-buster
RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app","--reload","--host","0.0.0.0"]