from data import db_session, users_resource
from flask import Flask, render_template, redirect
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)
api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:news_id>')

def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()


if __name__ == '__main__':
    main()