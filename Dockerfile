FROM  amd64/python:3.9

WORKDIR /Server

COPY . /Server

EXPOSE 5050

ENV NAME testserver

CMD ["python3", "-u", "Server.py"]
