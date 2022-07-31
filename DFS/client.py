from DFS import dfs

graph = {"Cairo": ["Zagazig", "Suez", "Giza"],
         "Giza": ["Alexandria", "North Coast"],
         "Suez": ["Gouna", "Hurghada"],
         "Zagazig": ["Mansoura"],
         "Fayoum": ["Qena"]
         }


def checkCoffeShop(node):
    if node is None:
        return False
    shops = {"Cairo": ["KFC", "MC", "Shawerma"],
             "Giza": ["TEA SHOP", "COFFEE SHOP"],
             "Suez": ["Fruits Shop", "KFC"],
             "Zagazig": ["MC"],
             "Fayoum": ["MC"]
             }
    if shops.get(node) is not None:
        for shop in shops.get(node):
            if shop == "COFFEE SHOP":
                return True
    return False


node = dfs(graph, "Cairo", checkCoffeShop)

print(f'{node } has an amazing COFFEE SHOP')
print(node)
