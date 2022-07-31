from BreadthFirstSearch import bfs
graph = {"Cairo": ["Zagazig", "Suez", "Giza"],
         "Giza": ["Alexandria", "North Coast"],
         "Suez": ["Gouna", "Hurghada"],
         "Zagazig": ["Mansoura"]
         }


isThereAPath = bfs(graph, "Cairo", "North Coast")
print(isThereAPath)
