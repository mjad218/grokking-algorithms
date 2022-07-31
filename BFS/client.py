from BreadthFirstSearch import bfs, displayPath
graph = {"Cairo": ["Zagazig", "Suez", "Giza"],
         "Giza": ["Alexandria", "North Coast"],
         "Suez": ["Gouna", "Hurghada"],
         "Zagazig": ["Mansoura"],
         "Fayoum": ["Qena"]
         }


path = bfs(graph, "Cairo", "North Coast")
print(path)

print(path.get("North Coast"))
print(displayPath(path,  "Cairo", "North Coast"))
# print(    f'There is {"a" if isThereAPath else "no"} path from Cairo to North Coast')

isThereAPath = bfs(graph, "Cairo", "Qena")
# print(f'There is {"a" if isThereAPath else "no"} path from Cairo to Qena')
