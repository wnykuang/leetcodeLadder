from flask import Flask
from flask_dynamo import Dynamo


class Databaseinitializer:
    def __init__(self, app: Flask):
        self.db = Dynamo(app)
        self.app = app

    def initialize(self):
        self.app.config['DYNAMO_ENABLE_LOCAL'] = True
        self.app.config['DYNAMO_LOCAL_HOST'] = 'localhost'
        self.app.config['DYNAMO_LOCAL_PORT'] = 8000
        self.app.run()
        return self.app

    def create_table(self, table_name: str, schema: dict):
        self.db.tables[table_name].create_table(**schema)
        return self.db.tables[table_name]