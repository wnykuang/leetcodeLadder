from flask import Flask
from database.databaseinitializer import Databaseinitializer


def create_app():
    flaskapp = Flask(__name__)
    dbinit = Databaseinitializer(flaskapp)
    dbinit.initialize()
    flaskapp.run()
    return flaskapp


app = create_app()


@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return f"{app.config['DYNAMO_LOCAL_HOST']}:{app.config['DYNAMO_LOCAL_PORT']}"


if __name__ == '__main__':
    app.run()
