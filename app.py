from flask import Flask, jsonify, request
import json

app = Flask(__name__)

db = {
    "bellevue": {
        "buildings": {
            "a": {"b": 1},
            "b": {"a": 5}
        }
    },
    "redmond": {
        "buildings": {
            "a": {"b": 5},
            "b": {
                "a": 10,
                "c": 2},
            "c": {}
        }
    }
}

knownDistances = {}

def depth_first_search(mapId, startId, stopId):
    # if valid return true, else return an error code
    # https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
    
    if True:
        return True
    else:
        return False


def dijkstras(mapId, startId, endId):
    # build the list of nodes based off of the mapId
    nodes = []
    for i in db[mapId]["buildings"]:
        nodes.append(i)

    # build the dictionary od distances
    distances = db[mapId]["buildings"]
    
    unvisited = {node: None for node in nodes} #using None as +inf
    visited = {}
    current = startId
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    
    print(visited)
    # known_distances[mapId][startId] = visited
    print(type(visited))
    print(endId)
    print(type(endId))
    distanceAnswer = visited[endId]
    path = []

    return distanceAnswer, path


# http://127.0.0.1:5000/maps/bellevue/path/A/B
# Accept: application/json
@app.route("/maps/<string:mapId>/path/<string:startId>/<string:endId>", methods=['GET'])
def find_shortest_route(mapId, startId, endId):
    # input validation
    # REFACTOR INTO SEPARATE FUNCTION
    if mapId.isalpha() == True and mapId.lower() in db:
        pass
    else:
        return {"message": "Map 'mapId' is unknown"}, 400
    
    if startId.isalpha() == True and startId.lower() in db[mapId]["buildings"]:
        pass
    else:
        return {"message": "Start 'startId' is unknown"}, 400

    if endId.isalpha() == True and endId.lower() in db[mapId]["buildings"]:
        pass
    else:
        return {"message": "End 'endId' is unknown"}, 400

    mapId = mapId.lower()
    startId = startId.lower()
    endId = endId.lower()

    # check memo
    # if startId in knownDistances[mapId]:
    #     print("HAPPENED")
    #     return jsonify({
    #         "distance": knownDistances[mapId][startId][endId],
    #         "path": [] # THIS NEEDS TO BE ADDED
    #     }), 200

    # check if a valid path exists
    if depth_first_search(mapId, startId, endId) == False:
        return {"message": "There is no path between 'startId' and 'endId'."}, 400

    # get distance using dijkstra's
    distanceAnswer, pathAnswer = dijkstras(mapId, startId, endId)

    return jsonify({
        "distance": distanceAnswer,
        "path": pathAnswer
    }), 200


# http://127.0.0.1:5000/maps/bellevue
# Content-Type: application/json
@app.route("/maps/<string:mapId>", methods=['PUT'])
def modify_map(mapId):
    # curl -H "Content-Type: application/json" -X PUT -d '{"buildings": { "a": { "b": 1 }, "b": {"a": 3}}}' http://127.0.0.1:5000/maps/bellevue
    try:
        jsonReceived = request.get_json()
        # IMPROVE BY HANDINGLING PARTIAL UPDATES
        # if mapId in db:
        #     # for building in jsonReceived:
        #     #     db[mapId]
        db[mapId] = jsonReceived
        print(db)
        # knownDistances[mapId] = {}
        return {}, 204
    except:
        return {"message": "The map data is invalid"}, 400


if __name__ == "__main__":
    app.run(debug=True)
