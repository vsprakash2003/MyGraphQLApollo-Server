from flask import Flask
from flask_graphql import GraphQLView
from database.database import Base, db_session
from schema.schema import schema
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.debug = True
CORS(app)

migrate = Migrate(app, Base)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        '/graphql',
        schema=schema,
        graphiql=True
                )
)


@app.route('/')
def welcome():
    return """Welcome to my application"""


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(threaded=True)