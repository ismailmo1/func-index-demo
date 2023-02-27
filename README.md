# Functional Indexes

This demo supports [this blog post](https://blog.ismailmo.com) on flask-security and functional indexes, It includes a simple flask app that uses flask-security for login/auth stuff, postgres for the db, and locust to do load testing on login times before and after adding a functional index.

## Setup

1. clone this repo and run `docker compose up -d` to run the flask app

2. you can then seed the postgres database with a bunch of user data using [this sql script](./load_testing/seed_emails.sql) 

3. To carry out load testing, open the locust webserver at [localhost:8089](localhost:8089) and start a new test setting `http://web:5000` (the flask app) as the host
