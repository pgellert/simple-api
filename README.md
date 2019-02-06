[![Build Status](https://travis-ci.org/pgellert/simple-api.svg?branch=master)](https://travis-ci.org/pgellert/simple-api)
# simple-api

This is a simple API that can store a list of groceries

Tools used:
  * Django
  * Django Rest Framework
  * Docker
  * Travis CI
  * Flake8

## Usage

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequently, the API responses are going to denote the content of the *`data`* field


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


### Add/Update grocery in list

*** Definition

`PUSH /groceries`

*** Arguments

  - `"name":string` the name of the grocery (unique identifier)
  - `"amount":string` the amount of the grocery needed
  - `"msg":string` any extra information

If a grocery with the same name exists, it gets updated (overwritten) by this request

*** Response

  - `201 Created` on success

  ```json
  {
    "name": "milk",
    "amount": "2",
    "msg": "Needed for cake"
  }
  ```


### Delete grocery from list

*** Definition

`DELETE /groceries/<name>`

*** Response

  - `404 Not Found` if no such grocery in list
  - `204 No Content` on success
