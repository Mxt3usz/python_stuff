recipes = {"Pizza Margherita": ["Mehl", "Hefe", "Tomaten"],
            "Pasta Napoli":     ["Penne", "Tomaten"],
            "Nudelauflauf":     ["Penne", "Käse", "Eier", "Sahne"]}

def cluster_by_ingredients(recipes):
    res = {}
    for key,val in recipes.items():
        for elements in val:
            if elements in res:
                res[elements] += [key]
            else:
                res.__setitem__(elements,[key])
    return res




print(cluster_by_ingredients(recipes))
