from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
from bson.json_util import dumps
import os


# USER = config('USER')
# PASSWD = config('PASSWD')

app = Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb+srv://'+ USER + ':' + PASSWD + '@cluster0-pgnge.mongodb.net/db_rendafixa?retryWrites=true&w=majority'
app.config['MONGO_URI'] = 'mongodb+srv://ricaportela:ricaportela@cluster0-pgnge.mongodb.net/db_rendafixa?retryWrites=true&w=majority'

mongo = PyMongo(app)
APP_URL = "http://0.0.0.0:5000"


class get_all_transactions(Resource):
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



class get_transaction_by_id(Resource):
    def get(self, id):
        transaction = mongo.db.transactions

        q = transaction.find_one({'id' : id})

        if q:
            output = {'id' : q['id'], 
                      'data' : q['data'],
                      'hora' : q['hora'],
                      'containicial' : q['containicial'],
                      'contafinal' : q['contafinal'],
                      'valor' : q['valor']
                    }
        else:
            output = 'No transaction found'

        return jsonify({'result' : output})


class Transaction(Resource):
#   def get(self):
#       return ({'name': "get message"}) 

    def post(self):
        return ({'name': "post message"})
    
    def put(self):
        return ({'name': "put message"})

    def delete(self):
        return ({'name': "delete message"})

class Search(Resource):
    def post(self):
        return ({'name': "search dates"})

api = Api(app)
api.add_resource(get_all_transactions, "/Transactions",  endpoint="transactions")
api.add_resource(Transaction, "/Transaction",  endpoint="transaction")
api.add_resource(get_transaction_by_id, "/TransactionById/<int:id>",  endpoint="transactionbyid")
api.add_resource(Search, "/Search",  endpoint="search")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



""" @app.route('/search', methods=['POST'])
def filter_entry():
    start = parse(request.form['start'])
    end = parse(request.form['end'])
    cur = mongo.db.transaction.find({'birthday': {'$lt': end, '$gte': start}})
    results = []
    for row in cur:
        results.append({"name": row['name'], "birthday": row['birthday'].strftime("%Y/%m/%d")})

    return render_template('result.html', results=results)
 """


