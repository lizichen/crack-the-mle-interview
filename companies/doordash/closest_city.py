"""
Get Closest City

A number of cities are arranged on a graph that has been divided up like an ordinary Cartesian plane. Each city is located at an integral (x, y) coordinate intersection. City names and locations are given in the form of three arrays: c, x, and y, which are aligned by the index to provide the city name (c[i]), and its coordinates, (x[i], y[i]). Determine the name of the nearest city that shares either an x or a y coordinate with the queried city. If no other cities share an x or y coordinate, return 'NONE'. If two cities have the same distance to the queried city, q[i], consider the one with an alphabetically shorter name (i.e. 'ab' < 'aba' < 'abb') as the closest choice. The distance is the Manhattan distance, the absolute difference in x plus the absolute difference in y.

"""
cities = ["a", "b", "c", "d", "e", "f", "g", "h"]
xValues = [0,1,2,4,5,0,1,0]
yValues = [1,2,5,3,4,2,0,2]
queries = ["a", "b", "c", "blah"]


city_map = {}
for i in range(len(cities)):
    city_map[cities[i]] = i
    
def get_closest_city(query_city):
    if query_city not in city_map:
        return 'None'
    
    q_idx = city_map[query_city]
    q_x = xValues[q_idx]
    q_y = yValues[q_idx]
    
    min_d = float('inf')
    min_idx = []
    
    for i in range(len(xValues)):
        if i == q_idx:
            continue
            
        x, y = xValues[i], yValues[i]
        if x == q_x or y == q_y:
            curr_d = abs(q_x - x) + abs(q_y - y)
            
            if curr_d < min_d:
                min_d = curr_d
                min_idx = [i]
            elif curr_d == min_d:
                min_idx.append(i)
    
    if min_idx == []:
        return None
    else:
        return sorted([cities[i] for i in min_idx])[0]

# test:
for q in queries:
    print(get_closest_city(q))