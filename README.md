# Techtest

This project is a technical test to store data into a database.


## How to use

#### Infrastructure

To launch the infrastructure needed (database), we use Docker and Docker-compose:

```
$ docker-compose up -d
```

#### Back-end

To launch the backend, we need first to create a virtualenv and install the requirements once:

```
$ cd back/
$ virtualenv --python=python3 venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Then, everytime, to launch the API:

```
$ cd back/
$ source venv/bin/activate
(venv) $ python run.py
```

Or, to launch the CLI interface:

```
$ cd back/
$ source venv/bin/activate
(venv) $ python -m techtest
```
