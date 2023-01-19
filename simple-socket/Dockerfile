FROM i386/python:3.10-alpine

COPY simple-socket/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV APP_NAME simple-socket
WORKDIR /usr/local/src/${APP_NAME}
COPY simple-socket/socket_server.py .

ENTRYPOINT [ "python", "socket_server.py" ]

EXPOSE 55555
