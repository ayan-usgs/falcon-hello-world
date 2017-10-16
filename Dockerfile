FROM alpine:3.6
MAINTAINER Andrew Yan "ayan@usgs.gov"
ARG artifact_version
ARG ssl_keyfile
ARG ssl_certfile
ARG build_type
ARG listening_port=7010
RUN apk update && apk upgrade && mkdir /local
RUN apk add --update \
  python3 \
  python3-dev \
  build-base \
  ca-certificates \
  openssl
RUN update-ca-certificates
COPY gunicorn_config.py /local/gunicorn_config.py
RUN export PIP_CERT="/etc/ssl/certs/ca-certificates.crt" && \
    pip3 install --upgrade pip && \
    pip3 install --extra-index-url https://cida.usgexis.gov/artifactory/api/pypi/usgs-python-${build_type}/simple -v falcon-hello-world==${artifact_version}
ENV bind_ip 0.0.0.0
ENV bind_port ${listening_port}
ENV ssl_keyfile ${ssl_keyfile}
ENV ssl_certfile ${ssl_certfile}
ENV log_level INFO
EXPOSE ${bind_port}
CMD ["/usr/bin/gunicorn", "--reload",  "greetings.app", "--config", "file:/local/gunicorn_config.py"]
