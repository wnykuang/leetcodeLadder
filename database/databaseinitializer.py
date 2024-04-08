import json
import os

from flask import Flask
from flask_dynamo import Dynamo
from boto3.session import Session


class Databaseinitializer:
    def __init__(self, app: Flask):
        os.environ["AWS_ACCESS_KEY_ID"] = ''
        os.environ["AWS_SECRET_ACCESS_KEY"] = ''
        self.app = app
        self.app.config['DYNAMO_ENABLE_LOCAL'] = True
        self.app.config['DYNAMO_LOCAL_HOST'] = 'localhost'
        self.app.config['DYNAMO_LOCAL_PORT'] = 8000

    def initialize_table(self, schemaJsonPath: str):
        if not os.path.exists(schemaJsonPath):
            raise Exception("Schema not found")
        with open(schemaJsonPath) as f:
            schema = json.load(f)

        self.app.config["DYNAMO_TABLES"] = [schema]
        self.db = Dynamo(self.app)
        with self.app.app_context():
            print(self.db.tables.keys())
            self.db.destroy_all()
    def clean_tables(self):
        with self.app.app_context():
            self.db.destroy_all()