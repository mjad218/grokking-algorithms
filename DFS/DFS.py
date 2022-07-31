# for the depth first search
# I just start at the node 0
# check if it is my desired node or if it has some things i want
# if so do what you want and return
# else loop through its neighbors and apply DFS on them
# just keep an array of visited nodes
# so you don't visit them twice


# EXAMPLE
# check if a certain city has an amazing COFFEE SHOP🔥

shops = {"Cairo": ["KFC", "MC", "Shawerma"],
         "Giza": ["TEA SHOP", "COFFEE SHOP"],
         "Suez": ["Fruits Shop", "KFC"],
         "Zagazig": ["MC"],
         "Fayoum": ["MC"]
         }

graph = {"Cairo": ["Zagazig", "Suez", "Giza"],
         "Giza": ["Alexandria", "North Coast"],
         "Suez": ["Gouna", "Hurghada"],
         "Zagazig": ["Mansoura"],
         "Fayoum": ["Qena"]
         }


def dfs(graph, node, target, visited={}):
    if visited.get(node):
        return None
    if target != None and target(node):
        return node

    visited[node] = True
    if graph.get(node) is not None:
        for city in graph.get(node):
            result = dfs(graph, city, target, visited)
            if result is not None:
                return result
