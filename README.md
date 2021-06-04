# capstone-project

## My project is live at https://nicg-capstone.herokuapp.com/

My motivation for this project is to finish the Full Stack program and finish the nanodegree.


There is no front-end since that is not a requirement for the project.

Actor Token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJNNGFHOFUwTWkxVDcwdC1DemI5ciJ9.eyJpc3MiOiJodHRwczovL2Rldi12cnhyejNoMy51cy5hdXRoMC5jb20vIiwic3ViIjoiT2E1eUpCRDdBZ3h0NUVNeWZzR0c4Ym5FVVA2M0FkYUVAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8veW91cmxvY2FsYXBpLmNvbS9haXAiLCJpYXQiOjE2MjI4MjQxNTksImV4cCI6MTYyMzAyNDE1OSwiYXpwIjoiT2E1eUpCRDdBZ3h0NUVNeWZzR0c4Ym5FVVA2M0FkYUUiLCJzY29wZSI6ImdldDphY3RvcnMgZ2V0OmFjdG9yc2FuZG1vdmllcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzYW5kbW92aWVzIl19.GUmP87-qtX0JLGPi-a0CM0-oXgbLmgBrt4oKvwzrikDfjler6p11-MetBeeQHDw_nGQ0zZFH9NAAAS33AobQPSXgh77WfUEVDNg9F_pp2Amd8fDtzj-uSfV_Wfx2GhC9NAXXy632UHuyDrhPFaRuhLLfaMKaxJfnYzUmA3XQtTxVI36N42kHbSe4P28nnLq7_cCH36uZKBNzJ34M7QYeo-v8HaKStT4ms9_wUWqb16RRnukjliBEQm9uOKFhd0s85UD19sy5_RGWvU1K6xwVNdp0ScFtTlux4jBm3yXpq0XxtbysbsNWVLVvEl0gvkvd1h0dWIf3m8jDCzGA7oonfw

Casting Director Token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJNNGFHOFUwTWkxVDcwdC1DemI5ciJ9.eyJpc3MiOiJodHRwczovL2Rldi12cnhyejNoMy51cy5hdXRoMC5jb20vIiwic3ViIjoiSnZKQktOQ0Y2RlVETkh0d2NkNzZ2VGxXUzBGV0U3MXJAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8veW91cmxvY2FsYXBpLmNvbS9haXAiLCJpYXQiOjE2MjI4MjQzMzAsImV4cCI6MTYyMzAyNDMzMCwiYXpwIjoiSnZKQktOQ0Y2RlVETkh0d2NkNzZ2VGxXUzBGV0U3MXIiLCJzY29wZSI6ImdldDphY3RvcnMgZ2V0OmFjdG9yc2FuZG1vdmllcyBkZWxldGU6YWN0b3JzIHBhdGNoOmFjdG9yc2FuZG1vdmllcyBhZGQ6YWN0b3JzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDphY3RvcnNhbmRtb3ZpZXMiLCJkZWxldGU6YWN0b3JzIiwicGF0Y2g6YWN0b3JzYW5kbW92aWVzIiwiYWRkOmFjdG9ycyJdfQ.a7WWiCH6K0VWmVXQ5ttTSZ9Khf-PwRyuxguVXmQRqsAoMMhfekZF3UntUJGYa1_vJFhduGkab0xwAaetYSVS9NY2xhyOzusUKjCBHyUG5mCzLt5yR9HywzQHjxL6DpYuPOuxsdhEoL4a5fEgJvpab6TvYPZebFqeEwmk4oq5nu0Oj1Ix2qQY4kS2KndTGeHLp2yNxn7m5aZhm5runCozlf9lrrASLIblDcs2sLqivyM7inwhC0rdEyLsx0mgEucpMQMSgD-LgARLDT7nJY3EM5ncFspPJ9pKRyZDEoEy9NQGBIcUhEp7TXbreR8caX2QXLKcEL4_98lWEq_3mBsGSg

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Database Setup

With Postgres running, run these commands to migrate database:

```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## Running the server

To run the server, execute:

```bash
python3 app.py
```

## Endpoints request & respose examples

`Note:` All Endpoints require authentication token except the home endpoint (`/`)



### Getting Bearer Tokens:

Please use the following Curl request to receieve updated bearer tokens:

curl --request POST \
  --url https://dev-vrxrz3h3.us.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data '{"client_id":"sCTwAvdVTzxDV991O8Yd6dHUvNdhZFC3","client_secret":"5uHxxUmqp2-m-cncSGj_F3GPFwNtnWzIdDp-Ysmb-MNWF2vaEnFyH_CS8f8YkUYS","audience":"https://yourlocalapi.com/aip","grant_type":"client_credentials"}'

### GET '/actors'

- request actors in the database
- Returns:Json opject contains {'succes': True, 'actors': []}
- **sample :** `curl https://nicg-capstone.herokuapp.com/actors -H "Authorization: Bearer <ACCESS_TOKEN>"`

```
{
  "actors": [
    {
      "age": 15,
      "gender": "female",
      "id": 1,
      "name": "Nada"
    },
    {
      "age": 15,
      "gender": "female",
      "id": 5,
      "name": "Mayar"
    }
  ],
  "success": true
}
```

### GET '/movies'

- request movies in the database
- Returns:Json opject contains {'succes': True, 'movies': []}
- **sample :** `curl https://nicg-capstone.herokuapp.com/movies -H "Authorization: Bearer <ACCESS_TOKEN>"`

```
{
  "movies": [
    {
      "id": 1,
      "release_date": "Tue, 10 Dec 2024 00:00:00 GMT",
      "title": "shs movie"
    },
    {
      "id": 4,
      "release_date": "Tue, 10 Dec 2024 00:00:00 GMT",
      "title": "super man"
    },
    {
      "id": 6,
      "release_date": "Tue, 10 Dec 2024 00:00:00 GMT",
      "title": "myshs movie"
    }
  ],
  "success": true
}
```

### DELETE '/actors/<int:id>'

- delete a single actor by id
- Returns: Json opject contains {'succes': True, 'deleted_actor': {}}
- **sample :** `curl -X DELETE https://nicg-capstone.herokuapp.com/actors -H "Authorization: Bearer <ACCESS_TOKEN>"`

```
{
 "deleted_actor": {
   "age": 15,
   "gender": "female",
   "id": 1,
   "name": "Hudaasa"
 },
 "success": true
}
```

### DELETE '/movies/<int:id>'

- delete a single movie by id
- Returns: Json opject contains {'succes': True, 'deleted_movie': {}}
- **sample :** `curl -X DELETE https://nicg-capstone.herokuapp.com/movies -H "Authorization: Bearer <ACCESS_TOKEN>"`

```
{
 "deleted_movie": {
     "id": 1,
     "release_date": "Tue, 10 Dec 2024 00:00:00 GMT",
     "title": "shs movie"
   },
 "success": true
}
```

### POST '/actors'

- create new actor
- Request Arguments: json object contains (name, age, gender)
- Returns: Json opject contains {'succes': True, 'new_actor': {}}
- **sample :** `curl -X POST https://nicg-capstone.herokuapp.com/actors -H "Authorization: Bearer <ACCESS_TOKEN>" -d '{"name":"xox","age":15,"gender":"male"}'`

```
{
  "new_actor": {
    "age": 15,
    "gender": "male",
    "id": 6,
    "name": "xox"
  },
  "success": true
}
```

### POST '/movies'

- create new movie
- Request Arguments: json object contains (title, year, month, day)
- Returns: Json opject contains {'succes': True, 'new_movie': {}}
- **sample :** `curl -X POST https://nicg-capstone.herokuapp.com/movies -H "Authorization: Bearer <ACCESS_TOKEN>" -d '{"title": "End World","year": 2024,"month": 12,"day": 10}'`

```
{
  "new_movie": {
    "id": 7,
    "release_date": "Tue, 10 Dec 2024 00:00:00 GMT",
    "title": "End World"
  },
  "success": true
}
```

### PATCH '/actors/<int:id>'

- modify specific actor by id
- Request Arguments: json object contains at least one of these values (name, age, gender)
- Returns: Json opject contains {'succes': True, 'modified_actor': {}}
- **sample :** `curl -X PATCH https://nicg-capstone.herokuapp.com/actors/6 -H "Authorization: Bearer <ACCESS_TOKEN>" -d '{"name":"test"}'`

```
{
  "modified_actor": {
    "age": 15,
    "gender": "male",
    "id": 6,
    "name": "test"
  },
  "success": true
}
```

### PATCH '/movies/<int:id>'

- modify specific movie by id
- Request Arguments: json object contains at least one of these values (title, year, month, day)
- Returns: Json opject contains {'succes': True, 'modified_movie': {}}
- **sample :** `curl -X PATCH https://nicg-capstone.herokuapp.com/movies/7 -H "Authorization: Bearer <ACCESS_TOKEN>" -d '{"year":2026}'`

```
{
  "modified_movie": {
    "id": 7,
    "release_date": "Thu, 10 Dec 2026 00:00:00 GMT",
    "title": "End World"
  },
  "success": true
}
```

## API RBAC

Our API have **2** roles :

### Actor

- Can view actors and movies

### Casting Director

- All permissions an actor has
- Add or delete an actor from the database
- Modify actors or movies

## Testing

there is a Postman test collection included within the project files
you can use it for testing
