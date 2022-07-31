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


def bfs(graph, start, end):
    queue = []
    queue.append(start)
    while len(queue) != 0:
        currentCity = queue.pop(0)
        if currentCity == end:
            return True
        if graph.get(currentCity) is not None:
            for city in graph[currentCity]:
                queue.append(city)

    return False
