import os
import sys
from flask import Flask, request, abort, jsonify, render_template, redirect, url_for, json, session, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode
from os import environ as env
from werkzeug.exceptions import HTTPException
from dotenv import load_dotenv, find_dotenv
from functools import wraps

from models import setup_db, Actor, Movie

from auth import AuthError, requires_auth

ACTORS_PER_PAGE = 10

app = Flask(__name__)

oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id='E2CCJ3PsZlTz2UPsumHaaGbhPfMTzvHP',
    client_secret='dbd-OlSfN7ZgyjMVa0fOUCpxsbiFSB6vJ5x84WlHqX6uyuQw5DGIJahfcu3VoWes',
    api_base_url='https://dev-vrxrz3h3.us.auth0.com',
    access_token_url='https://dev-vrxrz3h3.us.auth0.com/oauth/token',
    authorize_url='https://dev-vrxrz3h3.us.auth0.com/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)

database_path = os.environ['DATABASE_URL']
auth0_domain = os.environ['AUTH0_DOMAIN']
api_audience = os.environ['API_AUDIENCE']
client_id = os.environ['CLIENT_ID']
application_url = os.environ['APP_URL']

def paginate_actors(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * ACTORS_PER_PAGE
    end = start + ACTORS_PER_PAGE

    actors = [actor.format() for actor in selection]
    current_actors = actors[start:end]

    return current_actors


# App Config.

def create_app(test_config=None):

  # create and configure the app

    app = Flask(__name__)
    setup_db(app, database_path)
    CORS(app)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    app.config['SECRET_KEY'] = 'randomkey'

    @app.route('/')
    def index():

        return 'Welcome to the CapStone Project of Nicholas Greiner'

    @app.route('/login')
    def login():
        return auth0.authorize_redirect(redirect_uri='https://nicg-capstone.herokuapp.com/')

    @app.route('/login-result', methods=['GET'])
    def after_login():
        return jsonify({
            'success': True,
            'message': 'Successful login. Get token from address bar.'
        })

    @app.route('/callback')
    def callback_handling():
        # Handles response from token endpoint
        auth0.authorize_access_token()
        resp = auth0.get('userinfo')
        userinfo = resp.json()

        # Store the user information in flask session.
        session['jwt_payload'] = userinfo
        session['profile'] = {
            'user_id': userinfo['sub'],
            'name': userinfo['name'],
            'picture': userinfo['picture']
        }
        return redirect('/')    
      
    #  Get All the Actors

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actorsandmovies')
    def retrieve_actors(payload):

        actors = Actor.query.order_by(Actor.id).all()
        current_actors = paginate_actors(request, actors)

        if len(current_actors) == 0:
            abort(404)

        total_actors = len(Actor.query.all())

        return jsonify({'success': True, 'actors': current_actors,
                       'total_actors': total_actors})

    #  Get all the Movies

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:actorsandmovies')
    def retrieve_movies(payload):

        movies = Movie.query.order_by(Movie.id).all()
        current_movies = paginate_actors(request, movies)

        if len(current_movies) == 0:
            abort(404)

        total_movies = len(Movie.query.all())

        return jsonify({'success': True, 'movies': current_movies,
                       'total_movies': total_movies})

    #  Delete actor

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload):

        try:

            actor = Actor.query.get(id)

            if actor is None:
                abort(404)

            actor.delete()

            actors = Actor.query.order_by(Actor.id).all()
            current_actors = paginate_actors(request, actors)

            total_actors = len(Actor.query.all())

            return jsonify({
                'success': True,
                'deleted': actor.id,
                'actors': current_actors,
                'total_actors': total_actors,
                })
        except:

            abort(422)

    #  Delete movie

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_movie(payload):

        try:

            movie = Movie.query.get(id)

            if movie is None:
                abort(404)

            movie.delete()

            movies = Movie.query.order_by(Movie.id).all()
            current_movies = paginate_actors(request, movies)

            total_movies = len(Movie.query.all())

            return jsonify({
                'success': True,
                'deleted': movie.id,
                'movies': current_movies,
                'total_movies': total_movies,
                })
        except:

            abort(422)

    # Update actor

    @app.route('/actors/<int:actors_id>', methods=['PATCH'])
    @requires_auth('patch:actorsandmovies')
    def update_actor(token, actors_id):

        body = request.get_json()

        try:
            actor = Actor.query.filter(Actor.id
                    == actors_id).one_or_none()
            if actor is None:
                abort(404)

            if 'attributes_name' in body:
                actor.attributes_name = body.get('attributes_name')

                actor.update()

            return jsonify({'success': True, 'updated': actor.id})
        except:

            abort(400)

    # Update movie

    @app.route('/movies/<int:movies_id>', methods=['PATCH'])
    @requires_auth('patch:actorsandmovies')
    def update_movie(token, movies_id):

        body = request.get_json()

        try:
            movie = Movie.query.filter(Movie.id
                    == movies_id).one_or_none()
            if movie is None:
                abort(404)

            if 'attributes_title' in body:
                movie.attributes_title = body.get('attributes_title')

                movie.update()

            return jsonify({'success': True, 'updated': movie.id})
        except:

            abort(400)

    # Add new actor

    @app.route('/actors', methods=['POST'])
    @requires_auth('add:actors')
    def create_actor(payload):
        body = request.get_json()

        attributes_name = body.get('attributes_name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)

        try:
            actor = Actor(attributes_name=attributes_name, age=age,
                          gender=gender)
            actor.insert()

            selection = Actor.query.order_by(Actor.id).all()
            current_actors = paginate_actors(request, selection)

            total_actors = len(Actor.query.all())

            return jsonify({
                'success': True,
                'created': actor.id,
                'actors': current_actors,
                'total_actors': total_actors,
                })
        except:

            abort(422)

    # Add new movie

    @app.route('/movies', methods=['POST'])
    @requires_auth('add:actors')
    def create_movie(payload):
        body = request.get_json()

        attributes_title = body.get('attributes_title', None)
        release_date = body.get('release_date', None)
        actor_id = body.get('actor_id', None)

        try:
            movie = Movie(attributes_title=attributes_title,
                          release_date=release_date, actor_id=actor_id)
            movie.insert()

            selection = Movie.query.order_by(Movie.id).all()
            current_movies = paginate_actors(request, selection)

            total_movies = len(Movie.query.all())

            return jsonify({
                'success': True,
                'created': movie.id,
                'movies': current_movies,
                'total_movies': total_movies,
                })
        except:

            abort(422)

        # error Handling
        # 404

    @app.errorhandler(404)
    def not_found(error):
        return (jsonify({'success': False, 'error': 404,
                'message': 'Resource Not Found'}), 404)

        # 405

    @app.errorhandler(405)
    def method_not_allowed(error):
        return (jsonify({'success': False, 'eror': 405,
                'message': 'Method Not Allowed'}), 405)

        # 422

    @app.errorhandler(422)
    def unprocessable(error):
        return (jsonify({'success': False, 'error': 422,
                'message': 'Unprocessable'}), 422)

        # 400

    @app.errorhandler(400)
    def bad_request(error):
        return (jsonify({'success': False, 'error': 400,
                'message': 'Bad Request'}), 400)

        # 403

    @app.errorhandler(403)
    def forbidden(error):
        return (jsonify({'success': False, 'error': 403,
                'message': 'Forbidden'}), 403)

        # 500

    @app.errorhandler(500)
    def internal_server_error(error):
        return (jsonify({'success': False, 'error': 500,
                'message': 'Internal Server Error'}), 500)

        # error handler for AuthError

    @app.errorhandler(AuthError)
    def auth_error(e):
        return (jsonify(e.error), e.status_code)

    return app

app = create_app()

if __name__ == '__main__':
  app.run()