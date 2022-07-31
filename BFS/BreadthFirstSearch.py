# I assume i have the graph as a hash table
# where the value is an array of all the neighbors

# dict in python
# Cities in Egypt
graph = {"Cairo": ["Zagazig", "Suez", "Giza"],
         "Giza": ["Alexandria", "North Coast"],
         "Suez": ["Gouna", "Hurghada"],
         "Zagazig": ["Mansoura"],
         "Fayoum": ["Qena"]
         }

# I want to go from Cairo to North Coast
# start from cairo
# is cairo north coast? definitely not! add its neighbors to a queue
# check if the city at the front of the queue is north coast
# if true, just return
# if false, add its neighbors and repeat until you find the destination
# or the queue is empty


# now after implementing the algorithm, what if i want the path itself?
# well, for each node (or city), we can store the city that led to it.
def bfs(graph, start, end):
    visited = {}
    queue = []
    queue.append(start)
    while len(queue) != 0:
        currentCity = queue.pop(0)
        if currentCity == end:
            return visited
        if graph.get(currentCity) is not None:
            for city in graph[currentCity]:
                # {city : prevCity }
                # visitedCity = {city: currentCity}
                visited[city] = currentCity
                if visited.get(city) is not None:
                    queue.append(city)

    return False


# {"city" : "cairo", "prevCity": "Alex"}

def displayPath(visited, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = visited.get(current)
    path.append(current)
    path.reverse()
    return path
