import json
import os

from flask import Flask
from flask_dynamo import Dynamo
from decimal import Decimal


class Databaseinitializer:
    def __init__(self, app: Flask):
        os.environ["AWS_ACCESS_KEY_ID"] = ''
        os.environ["AWS_SECRET_ACCESS_KEY"] = ''
        self.app = app
        self.app.config['DYNAMO_ENABLE_LOCAL'] = True
        self.app.config['DYNAMO_LOCAL_HOST'] = 'localhost'
        self.app.config['DYNAMO_LOCAL_PORT'] = 8000
        self.db = Dynamo(self.app)

    def initialize_table(self, schemaJsonPath: str):
        """
        load the json schema
        :param schemaJsonPath:
        :return:
        """
        if not os.path.exists(schemaJsonPath):
            raise Exception("Schema not found")
        with open(schemaJsonPath) as f:
            schema = json.load(f)
        self.app.config["DYNAMO_TABLES"].append(schema)

    def write_data_to_table(self, csv_file_path: str, table_name: str):
        """
        write a function to write data to the dynamodb
        """
        with open(csv_file_path) as f:
            data = json.load(f, parse_float=lambda x: round(Decimal(x),2))

        if table_name not in self.db.tables.keys():
            raise Exception("Table not found")

        if table_name == "problemRating":
            for datrum in data:
                self.db.tables[table_name].put_item(Item={
                    "questionId": Decimal(datrum["question_id"]),
                    "questionRating": Decimal(datrum["rating"]),
                    "question_title": datrum["question_title"],
                    "dummyPartitionKey": datrum["question_id"]
                })
    def create_table(self):
        with self.app.app_context():
            self.db.create_all()