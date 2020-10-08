FROM ubuntu:20.04
COPY . /app
WORKDIR /app
RUN apt-get update && \
    apt-get install python3-pip -y && \
    pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]

