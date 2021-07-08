from typing import Iterator

def knapsack(goal : int, items : list[tuple[str,int]]) -> Iterator[list[str]]:
    if goal == 0:
        yield []
    elif not items:
        return
    else:
        name, weight = items[0]
        remaining_items = items[1:]
        yield from knapsack(goal, remaining_items) # solutions without item
        # now for the solutions including item name
        if weight <= goal:
            for solution in knapsack(goal - weight, remaining_items):
                yield [name] + solution

def knapsack_nocopy(goal : int, items : list[tuple[str,int]], i : int) -> Iterator[list[str]]:
    if goal == 0:
        yield []
    elif i >= len(items):
        return
    else:
        name, weight = items[i]
        yield from knapsack_nocopy(goal, items, i+1) # solutions without item
        # now for the solutions including item name
        if weight <= goal:
            for solution in knapsack_nocopy(goal - weight, items, i+1):
                yield [name] + solution

def knapsack_dict(goal: int, items : dict[str,int]) -> Iterator[list[str]]:
    return knapsack_nocopy(goal, list(items.items()), 0)

gifts = {'phone': 200, 'boots': 1200, 'laptop': 2200, 'glasses': 50,
         'camera': 150, 'jumpsuit': 2340, 'headphones': 80, 'fitbit': 40,
         'hanger': 10, 'pillow': 400, 'hoverboard': 870, 'handbag': 430}

kg500  = knapsack_dict(500, gifts)
kg2400 = knapsack_dict(2400, gifts)
kg4900 = knapsack_dict(4900, gifts)
## every next yields a list[str] of gifts that fit in the suitcase
