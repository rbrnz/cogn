#!/bin/bash
psql --command "CREATE USER airflow WITH SUPERUSER PASSWORD 'password';" -U postgres
psql --command "CREATE DATABASE airflow;" -U postgres
psql --command "CREATE DATABASE oltp;" -U postgres
psql --command "GRANT ALL PRIVILEGES ON airflow TO airflow;" -U postgres
psql --command "GRANT ALL PRIVILEGES ON oltp TO airflow;" -U postgres
