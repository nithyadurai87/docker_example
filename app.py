from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb',27017)
db = client.forest
collection = db.flowers

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        data = request.get_json()
        collection.insert_one(data).inserted_id
        with open('./tmpfiles/data.log','a') as f:
            f.write(str(data)+'/n')
        return ('', 204)
        
    if request.method == 'GET':
        data = collection.find()
        response = []
        for i in data:
            i['_id'] = str(i['_id'])
            response.append(i)
        return jsonify(response)
                
if __name__ == '__main__':
    app.run(host='0.0.0.0')

"""

curl --header "Content-Type: application/json" --request POST --data '{"lotus":10,"tulips":14}' localhost:5000

curl localhost:5000

"""
