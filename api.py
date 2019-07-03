from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
from bson.json_util import dumps
from decouple import config

USER = config('USER')
PASSWD = config('PASSWD')

app = Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb+srv://'+ USER + ':' + PASSWD + '@cluster0-pgnge.mongodb.net/db_rendafixa?retryWrites=true&w=majority'
app.config['MONGO_URI'] = 'mongodb+srv://ricaportela:ricaportela@cluster0-pgnge.mongodb.net/db_rendafixa?retryWrites=true&w=majority'

mongo = PyMongo(app)
APP_URL = "http://127.0.0.1:5000"


class Transaction_All(Resource):
    def get(self):
        transactions = mongo.db.transactions.find({})
        output = []
        for q in transactions:
            output.append({'id': q['id'],
                           'data': q['data'],
                           'hora': q['hora'],
                           'containicial': q['containicial'],
                           'contafinal': q['contafinal'],
                           'valor': q['valor']
            })

        return jsonify({'resultado': output})


class Transaction(Resource):
    def get(self):
        return ({'name': "get mensagem"})
    
    def post(self):
        return ({'name': "post mensagem"})
    
    def put(self):
        return ({'name': "put mensagem"})

    def delete(self):
        return ({'name': "delete mensagem"})

api = Api(app)
api.add_resource(Transaction_All, "/Transactions",  endpoint="transactions")
api.add_resource(Transaction, "/Transaction",  endpoint="transaction")


if __name__ == "__main__":
    app.run(debug=True)



""" @app.route('/search', methods=['POST'])
def filter_entry():
    start = parse(request.form['start'])
    end = parse(request.form['end'])
    cur = mongo.db.user.find({'birthday': {'$lt': end, '$gte': start}})
    results = []
    for row in cur:
        results.append({"name": row['name'], "birthday": row['birthday'].strftime("%Y/%m/%d")})

    return render_template('result.html', results=results)
 """


