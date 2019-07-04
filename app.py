import os
from flask import Flask, jsonify, url_for, redirect, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource


# USER = config('USER')
# PASSWD = config('PASSWD')

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://ricaportela:ricaportela@cluster0-pgnge.mongodb.net/db_rendafixa?retryWrites=true&w=majority'
mongo = PyMongo(app)
APP_URL = "http://127.0.0.1:5000"


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
        data = []
        if id:
            transaction_info = mongo.db.transactions.find_one({"id": id}, {"_id": 0})
            if transaction_info:
                return jsonify({"status": "ok", "data": transaction_info})
            else:
                return {"response": "no transaction found for {}".format(id)}

        return jsonify({"response": data})



class Transactions(Resource):
    #   def get(self):
    #       return ({'name': "get message"})

    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            id = data.get('id')
            if id:
                if mongo.db.transactions.find_one({"id": id}):
                    return {"response": "transaction already exists."}
                else:
                    mongo.db.transactions.insert(data)
            else:
                return {"response": "registration number missing"}

        return redirect(url_for("transaction"))


    def put(self):
        return ({'name': "put message"})

    def delete(self):
        return ({'name': "delete message"})



class Search(Resource):
    def post(self):
        # start = parse(request.form['start'])
        # end = parse(request.form['end'])
        # cur = mongo.db.transaction.find({'birthdataday': {'$lt': end, '$gte': start}})
        # results = []
        # for row in cur:
        # results.append({"name": row['name'], "birthday": row['birthday'].strftime("%Y/%m/%d")})
    
        return ({'name': "search dates"})



api = Api(app)
api.add_resource(get_all_transactions, "/get_all_transactions", endpoint="get_all_transactions")
api.add_resource(get_transaction_by_id, "/transactions/<int:id>",  endpoint="transactionbyid")
api.add_resource(Transactions, "/Transactions",  endpoint="transactions")
api.add_resource(Search, "/Search",  endpoint="search")


if __name__ == "__main__":
    app.run(debug=True)
