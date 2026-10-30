graph = {"Start" : {"A":2, "B":5, "C":4},
         "A" : {"B":1, "D":7},
         "B" : {"D":3, "E":6},
         "C" : {"B":2, "E":4},
         "D" : {"E":1, "Finish":2},
         "E" : {"Finish":3},
         "Finish" : {}}

costs = {"Start" : 0,
         "A" : float("inf"),
         "B" : float("inf"),
         "C" : float("inf"),
         "D" : float("inf"),
         "E" : float("inf"),
         "Finish" : float("inf")}

parents = {"Start" : None,
           "A" : None,
           "B" : None,
           "C" : None,
           "D" : None,
           "E" : None,
           "Finish" : None}

ticked = []

def find_cheapest():
    cheapest = None
    lowest = float("inf")
    for node in costs:
        if node not in ticked and costs[node] < lowest:
            lowest = costs[node]
            cheapest = node
    return cheapest

place = find_cheapest()
while place is not None:
    for neighbour in graph[place]:
        new_cost = costs[place] + graph[place][neighbour] 
        if new_cost < costs[neighbour]:
            costs[neighbour] = new_cost
            parents[neighbour] = place
    ticked.append(place)
    place = find_cheapest()

step = "Finish"
route = []
while step is not None:
    route.append(step)
    step = parents[step]

route.reverse()
print(route)
                    
