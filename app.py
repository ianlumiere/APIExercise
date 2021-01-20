from flask import Flask, jsonify, request
import json

app = Flask(__name__)

mock_list_db = [
    {
        "name": "Mew",
        "level": 5,
        "in_party": True
    },
    {
        "name": "Pikachu",
        "level": 32,
        "in_party": True
    }
]

# http://127.0.0.1:5000/
@app.route("/", methods=['GET', 'POST'])
def index():
    # curl -H "Content-Type: application/json" -X POST -d '{"name": "Poliwhirl", "level": 28, "in_party": false}' http://127.0.0.1:5000/
    if request.method == "POST":
        json_received = request.get_json()
        mock_list_db.append(json_received) # add it to the dictionary
        return jsonify({"JSON Sent": json_received}), 201
    else:
        return "Welcome to the API!", 200

with app.test_client() as c:
    rv = c.post('/', json={
        "name": "Poliwhirl", "level": 28, "in_party": False
    })
    json_data = rv.get_json()
    json_data = json.dumps(json_data, sort_keys=True)
    expected_data = json.dumps({'JSON Sent': {'in_party': False, 'level': 28, 'name': 'Poliwhirl'}}, sort_keys=True)
    assert json_data == expected_data


# http://127.0.0.1:5000/pokemon_list
@app.route("/pokemon_list", methods=['GET'])
def get_pokemon_list():
    return jsonify({"Pokemon": mock_list_db}), 200


# http://127.0.0.1:5000/pokemon_list/0
@app.route("/pokemon_list/<int:index>", methods=['GET', 'PUT', 'DELETE'])
def get_pokemon_by_index(index):
    # curl -H "Content-Type: application/json" -X PUT -d '{"name": "Mew", "level": 6, "in_party": false}' http://127.0.0.1:5000/pokemon_list/0
    if request.method == "PUT":
        json_received = request.get_json()
        for key in json_received:
            mock_list_db[index][key] = json_received[key]
        return jsonify({"Updated results": mock_list_db[index]}), 200
    # curl -X DELETE http://127.0.0.1:5000/pokemon_list/0
    if request.method == "DELETE":
        item_deleted = mock_list_db[index]["name"]
        del mock_list_db[index]
        return jsonify({"Deleted": item_deleted}), 204
    else:
        return jsonify({"Pokemon": mock_list_db[index]}), 200


# http://127.0.0.1:5000/multiply/5
@app.route("/multiply_ten/<int:value>", methods=['GET'])
def multiply_ten(value):
    return jsonify({"Result": value*10}), 200


# http://127.0.0.1:5000/author?name=Ian
@app.route("/author")
def get_author():
    name = request.args.get("name")
    return jsonify({"data": name}), 200


if __name__ == "__main__":
    app.run(debug=True)
