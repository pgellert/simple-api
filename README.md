[![Build Status](https://travis-ci.org/pgellert/simple-api.svg?branch=master)](https://travis-ci.org/pgellert/simple-api)
# simple-api

This is a simple API that can store a list of groceries. The api is available at http://simple-grocery-api.herokuapp.com/api/v1/groceries

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
      "pk": 12,
      "name": "milk",
      "amount": 2,
      "msg": "Needed for cake"
    },
    {
      "pk": 13,
      "name": "egg",
      "amount": 12,
      "msg": ""
    }
  ]
  ```


### Add grocery to list

*** Definition

`POST /groceries`

*** Arguments

  - `"name":string` the name of the grocery
  - `"amount":integer` the amount of the grocery needed
  - `"msg":string` any extra information

*** Response

  - `201 Created` on success
  - `400 Bad request` if the data is invalid

  ```json
  {
    "pk": 12,
    "name": "milk",
    "amount": 2,
    "msg": "Needed for cake"
  }
  ```


### Get grocery from list

*** Definition

`GET /groceries/<pk>`

*** Response

  - `200 OK` on success
  - `404 Not Found` if no such grocery in list

  ```json
  {
    "pk": 12,
    "name": "milk",
    "amount": 2,
    "msg": "Needed for cake"
  }
  ```


### Update grocery in list

*** Definition

`PUT /groceries/<pk>`

*** Arguments

  - `"name":string` the name of the grocery
  - `"amount":integer` the amount of the grocery needed
  - `"msg":string` any extra information

*** Response

  - `204 No Content` on success
  - `400 Bad request` if the data is invalid

  ```json
  {
    "pk": 12,
    "name": "milk",
    "amount": 2,
    "message": "Needed for cake"
  }
  ```


### Delete grocery from list

*** Definition

`DELETE /groceries/<pk>`

*** Response

  - `204 No Content` on success
  - `404 Not Found` if no such grocery in list
