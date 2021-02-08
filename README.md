# Python coding challenge

## Context

This project is a from a coding challenge.

* Build a rest api using python 3.
* Using the data from the attached CSV file, develop the following user story:

Story:
    To get a better view of data, a user can filter an indicator for getting countries which has greater index value than a filter(input) value

Scenario:
    User wants to get countries with  life satisfaction index value greater than an input value

* Given: All countries with their indicators loaded (from the dataset).
* When: A user wants to get countries with life satisfaction index greater than the input value.
* Then: Return countries with their index value, greater than the input value, using only life satisfaction index and total inequality

Keep in mind:
* The current api should be able to support new index filters.
* Use a rest framework (like Flask).
* Validate the input data.
* Create a ReadMe file where should be documented, how to implement and use the project.

## Project structure

```shell
api-challenge
|   docker-compose.yml
|   README.md
\---api
    |   app.py
    |   data.db
    |   db.py
    |   db_setup.py
    |   Dockerfile
    |   requirements.txt
    |   test_app.py
    +---data
    |       BLI_28032019144925238.csv
    +---models
    |       indicator.py
    |       __init__.py
    \---resources
            indicator.py
            __init__.py
```

## Getting Started

### Prerequisites

In order to run this container you'll need Docker and Docker Compose installed.

#### Docker

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

#### Docker Compose

* [Install Docker Compose](https://docs.docker.com/compose/install/)

### Usage

From the project directory run `docker-compose build` and then `docker-compose up`.

```shell
Starting api-challenge_web_1 ... done                                                                                   
Attaching to api-challenge_web_1
web_1  |  * Serving Flask app "app" (lazy loading)
web_1  |  * Environment: production
web_1  |    WARNING: This is a development server. Do not use it in a production deployment.
web_1  |    Use a production WSGI server instead.
web_1  |  * Debug mode: off
web_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

### Endpoints

* 127.0.0.1:5000/filter_country_by_indicator

In order to get countries with life satisfaction index greater than the input value make a POST request to this endpoint with the following json:

```shell
{
    "indicator_name": "Life satisfaction",
    "value": 7.5
}
```

This API supports new indexes, send other indicator name under de `indicator_name` key.
