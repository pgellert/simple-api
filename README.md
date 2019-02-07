[![Build Status](https://travis-ci.org/pgellert/simple-api.svg?branch=master)](https://travis-ci.org/pgellert/simple-api)
# simple-api

This is a simple API that can store a list of groceries

Tools used:
  * Django
  * Django Rest Framework
  * Docker
  * Travis CI
  * Flake8


### List groceries

*** Definition

`GET /groceries`

*** Response

  - `200 OK` on success

  ```json
  [
    {
      "id": "12",
      "name": "milk",
      "amount": "2",
      "msg": "Needed for cake"
    },
    {
      "id": "13",
      "name": "egg",
      "amount": "12",
      "msg": ""
    }
  ]
  ```


### Add grocery to list

*** Definition

`PUSH /groceries`

*** Response

  - `201 Created` on success
  - `400 Bad request` if the data is invalid

  ```json
  {
    "id": "12",
    "name": "milk",
    "amount": "2",
    "msg": "Needed for cake"
  }
  ```


### Get grocery from list

*** Definition

`GET /groceries/<id>`

*** Arguments

  - `"name":string` the name of the grocery
  - `"amount":string` the amount of the grocery needed
  - `"msg":string` any extra information

*** Response

  - `200 OK` on success
  - `404 Not Found` if no such grocery in list

  ```json
  {
    "id": "12",
    "name": "milk",
    "amount": "2",
    "msg": "Needed for cake"
  }
  ```


### Update grocery in list

*** Definition

`PUT /groceries/<id>`

*** Arguments

  - `"name":string` the name of the grocery
  - `"amount":string` the amount of the grocery needed
  - `"msg":string` any extra information

*** Response

  - `204 No Content` on success
  - `400 Bad request` if the data is invalid

  ```json
  {
    "id": "12",
    "name": "milk",
    "amount": "2",
    "msg": "Needed for cake"
  }
  ```


### Delete grocery from list

*** Definition

`DELETE /groceries/<id>`

*** Response

  - `204 No Content` on success
  - `404 Not Found` if no such grocery in list
