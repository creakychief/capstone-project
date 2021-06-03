# capstone-project

## My project is live at https://nicg-capstone.herokuapp.com/

There is no front-end since that is not a requirement for the project.

Actor Token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJNNGFHOFUwTWkxVDcwdC1DemI5ciJ9.eyJpc3MiOiJodHRwczovL2Rldi12cnhyejNoMy51cy5hdXRoMC5jb20vIiwic3ViIjoic0NUd0F2ZFZUenhEVjk5MU84WWQ2ZEhVdk5kaFpGQzNAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8veW91cmxvY2FsYXBpLmNvbS9haXAiLCJpYXQiOjE2MjI3NTkyMDEsImV4cCI6MTYyMjk1OTIwMSwiYXpwIjoic0NUd0F2ZFZUenhEVjk5MU84WWQ2ZEhVdk5kaFpGQzMiLCJzY29wZSI6ImdldDphY3RvcnMgZ2V0OmFjdG9yc2FuZG1vdmllcyBwYXRjaDphY3RvcnNhbmRtb3ZpZXMgYWRkOmFjdG9ycyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzYW5kbW92aWVzIiwicGF0Y2g6YWN0b3JzYW5kbW92aWVzIiwiYWRkOmFjdG9ycyJdfQ.cgTwZTugbyeZPU4tmCAt5Wo5qEWW0ZBbRWCN1_7GJcMGEbDX1hDhTMPeYvRBATCMvm32ZHJjqPniwvLpAi7RoW2MkwO5Fo4WI4EYVcrpUgWUkqe-h5CCr1cqaxRss42QkUeNDwFlATNGo_13SQmd1mp4s05hyA_l3Bem8IjE_Y9kPaUXNA2eyk2c4MspXn6DBUHInCeXpRtt3M3bbhzKeQPyX5numktjwmZGlGiC9JsDRf0HMCZOBTazaRj907YWPAbfEYdBwj2d2maBQdFouajXSVIX-g1bBRzzv2xcef7QocuOkAICSAEBbY9q4UM_iTR-LHSC_kFTDTeAhoV6_A

Casting Director Token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJNNGFHOFUwTWkxVDcwdC1DemI5ciJ9.eyJpc3MiOiJodHRwczovL2Rldi12cnhyejNoMy51cy5hdXRoMC5jb20vIiwic3ViIjoic0NUd0F2ZFZUenhEVjk5MU84WWQ2ZEhVdk5kaFpGQzNAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8veW91cmxvY2FsYXBpLmNvbS9haXAiLCJpYXQiOjE2MjI3NTkzMTMsImV4cCI6MTYyMjk1OTMxMywiYXpwIjoic0NUd0F2ZFZUenhEVjk5MU84WWQ2ZEhVdk5kaFpGQzMiLCJzY29wZSI6ImdldDphY3RvcnMgZ2V0OmFjdG9yc2FuZG1vdmllcyBwYXRjaDphY3RvcnNhbmRtb3ZpZXMgYWRkOmFjdG9ycyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzYW5kbW92aWVzIiwicGF0Y2g6YWN0b3JzYW5kbW92aWVzIiwiYWRkOmFjdG9ycyJdfQ.KQnc0WMfG6UF7aPV0mhvbrbOZZj_TJXi-2p8zIsUbmt5T9q3SJBQwoUtzZKzVpAbVZnyqikfVVMR_lPYzNG4x-GcBTbWrumg3NqVURfgdjYEAS0THk9g38qR7GUuuObAluHhhfHqXZhNFVkJ7pusnks54KrEQScGijucnUM39WmYSHO7IkhUBF3T3pLLnVxVOuINxTWek8941xeqyl1thefJam81rMiTbbiimskPvzrWx7CG3brdeXY8i7rS68_ziMQA6BV4drKYk-ViXMOqfxVIigL7l_8LKH5BBs4ugP2GF-TBdIeH8OveJMfdvb50JoWkHTNqmKHu7ypP8k2V7w

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

Our API have **3** roles :

### Casting Assistant

- Can view actors and movies

### Casting Director

- All permissions a Casting Assistant has
- Add or delete an actor from the database
- Modify actors or movies

### Executive Producer

- All permissions a Casting Director has
- Add or delete a movie from the database

## Testing

there is a Postman test collection included within the project files
you can use it for testing
