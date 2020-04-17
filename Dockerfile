FROM ubuntu:latest
EXPOSE 80
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip git nano
RUN pip3 install netaddr Flask requests
WORKDIR /app
RUN git clone https://github.com/collin-clark/docker-netulator.git .
ENTRYPOINT [“python3”]
CMD [“ipcalc.py”]
