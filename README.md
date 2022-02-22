# APIExercise
Repo for interview

# Problem Notes
buildings can be added, routes can change
looking for quickest route
need to keep mapping info up to date
THE GRAPH IS DIRECTED

create a rest endpoint that will accept a list of buildings and distances between them and to find the shortest path between them (Djkstra's) 

each campus is a map that consists of buildings and edges (directed connection between two buildings described by a distance)
campuses are complex and may have one or two way paths with different distances.
so A to B might be 2 
but B to A might be 5

each map is given an ID so the system can be used for multiple campuses

multiple campuses, multiple buildings per campus
Only need to find routes within one campus, not between campuses.
Locations are unique on a campus, but are NOT globally unique. so many campuses will have a building A

api has 2 main endpoints:
find_optimal_route
 GET /maps/{mapId}/path/{startId}/{endId}

create_or_update_map
PUT /maps/{mapId}