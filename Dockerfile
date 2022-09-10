FROM python:3.8
COPY . /api
WORKDIR /api
ENV PYTHONUNBUFFERED 1
RUN pip3 install -r requirements.txt
CMD ["python","application.py"]
