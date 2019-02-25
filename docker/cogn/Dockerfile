FROM ubuntu
RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apt-get install -y git

# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel

ENV ETL_HOME=/src/
RUN pip3 install \
    asn1crypto==0.24.0 \
    cryptography==2.1.4 \
    idna==2.6 \
    keyring==10.6.0 \
    keyrings.alt==3.0 \
    numpy==1.16.1 \
    pandas==0.24.1 \
    psycopg2==2.7.7 \
    psycopg2-binary==2.7.7 \
    pycrypto==2.6.1 \
    pygobject==3.26.1 \
    python-apt==1.6.3+ubuntu1 \
    python-dateutil==2.8.0 \
    pytz==2018.9 \
    pyxdg==0.25 \
    SecretStorage==2.3.1 \
    six==1.11.0 \
    SQLAlchemy==1.2.18 \
    unattended-upgrades==0.1

# Preparing for Airflow

#ENV SLUGIFY_USES_TEXT_UNIDECODE=yes
#ENV AIRFLOW_HOME=/src/etl
#RUN mkdir -m 777 -p $AIRFLOW_HOME

#RUN pip3 install apache-airflow
#RUN pip3 install apache-airflow[postgres]
#
#RUN airflow version

CMD ["/bin/bash"]
