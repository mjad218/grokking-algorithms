from BreadthFirstSearch import bfs
graph = {"Cairo": ["Zagazig", "Suez", "Giza"],
         "Giza": ["Alexandria", "North Coast"],
         "Suez": ["Gouna", "Hurghada"],
         "Zagazig": ["Mansoura"],
         "Fayoum": ["Qena"]
         }


isThereAPath = bfs(graph, "Cairo", "North Coast")
print(
    f'There is {"a" if isThereAPath else "no"} path from Cairo to North Coast')

isThereAPath = bfs(graph, "Cairo", "Qena")
print(f'There is {"a" if isThereAPath else "no"} path from Cairo to Qena')
