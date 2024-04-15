from flask import Flask, request, jsonify
from database.databaseinitializer import Databaseinitializer
from boto3.dynamodb.conditions import Key

def create_app():
    flaskapp = Flask(__name__)

    dbinit = Databaseinitializer(flaskapp)
    dbinit.initialize_table("static/ratingtableschema.json")
    dbinit.create_table()
    dbinit.write_data_to_table("static/problemRating.json", "problemRating")

    flaskapp.dbinit = dbinit
    return flaskapp


app = create_app()


@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return f"{app.config['DYNAMO_LOCAL_HOST']}:{app.config['DYNAMO_LOCAL_PORT']}"

@app.route('/problemRating/', methods=['GET'])
def get_problem_rating():
    lowerbound = request.args.get('l')
    upperbound = request.args.get('u')
    if lowerbound is None and upperbound is None:
        return jsonify({"error": "Invalid input"}), 400
    lowerbound = int(lowerbound)
    upperbound = int(upperbound)
    filterExpression = Key("questionRating").between(lowerbound, upperbound)
    for item in app.dbinit.db.tables["problemRating"].scan(FilterExpression=filterExpression)["Items"]:
        print(item)
    return "Problem rating"