from flask import Flask
from flask_dynamo import Dynamo
from database.databaseinitializer import Databaseinitializer


def create_app():
    flaskapp = Flask(__name__)
    dbinit = Databaseinitializer(flaskapp)
    dbinit.initialize_table("static/ratingtableschema.json")
    dbinit.clean_tables()
    # flaskapp.run()
    with flaskapp.app_context():
        dbinit.db.create_all()
    dbinit.db.destroy_all()
    return flaskapp

app = create_app()


@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return f"{app.config['DYNAMO_LOCAL_HOST']}:{app.config['DYNAMO_LOCAL_PORT']}"
