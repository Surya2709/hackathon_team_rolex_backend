FROM python:3.6
COPY . /api
WORKDIR /api
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt
CMD ["python","application.py"]
