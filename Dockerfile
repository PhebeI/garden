FROM python:3

RUN mkdir /app
ADD garden.py /app

WORKDIR /app

ENTRYPOINT ["python"]
CMD ["garden.py"]

