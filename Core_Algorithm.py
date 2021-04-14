import Distance
from WeightedGraph import *
import Packages
import datetime

package_graph = WeightedGraph()


# Function used to generate weighted graphs based on truck data
# Parameter: package id list Returns: package graph
# O(N)
def generate_graph(package_id_list):
    dist_id = [0]
    # convert ids
    for p in package_id_list:
        dist_id.append(Distance.pkg_d_keys.search_key(p))
    dist_id.append(0)  # hub
    # add vertices
    for v in Distance.distance_table.vertices:
        if dist_id.__contains__(v):
            package_graph.add_vertex(v)
    # add edges
    for v in package_graph.vertices:
        for u in package_graph.vertices:
            package_graph.add_edge(v, u, Distance.distance_table.distances.search_key((v, u)))
    return package_graph


# Nearest neighbor algorithm used to sort packages greedily
# Parameters: package graph, package id list
# O(NLog N)
def nearest_neighbor_sort(graph, package_id_list):
    min_index = 0
    new_list = [0]
    unvisited = [0]
    for p in package_id_list:
        unvisited.append(Distance.pkg_d_keys.search_key(p))
    unvisited.append(0)
    unvisited.pop(-1)
    u = unvisited.pop(0)
    while unvisited:
        min_dist = float('inf')
        for i in range(len(unvisited)):
            if graph.distances.search_key((u, unvisited[i])) < min_dist:
                min_dist = graph.distances.search_key((u, unvisited[i]))
                min_index = unvisited[i]
            if i == len(unvisited) - 1:
                unvisited.remove(min_index)
                u = min_index
                new_list.append(u)
    new_list.append(0)
    return new_list


# Two option algorithm swap function
# Switches two edges of the graph
# Parameters: starting route, swap starting index, swap ending index  Return: New route
# O(N)
def two_opt_swap(route, i, k):
    new_route = []
    for a in range(i - 1):
        new_route.append(route[a])
    for b in range(k, i - 2, -1):
        new_route.append(route[b])
    for c in range(k + 1, len(route), 1):
        new_route.append(route[c])
    return new_route


# Two option algorithm
# Compares different swap results and chooses the first improved one
# Repeats until no improvement is made
# O(N^3)
def two_opt(route):
    best_dist = route_distance(route)
    new_dist = 0
    existing_route = route
    while new_dist < best_dist:
        for i in range(2, len(route) - 1):
            for k in range(2, len(route) - 1):
                new_route = two_opt_swap(existing_route, i, k)
                new_dist = route_distance(new_route)
                if new_dist < best_dist:
                    existing_route = new_route
                    best_dist = new_dist
    return best_dist, existing_route


# Calculates total distance of a route
# O(N)
def route_distance(route):
    graph = generate_graph(route)
    route_dist = 0
    for v, v1 in enumerate(route):
        if v + 1 < len(route):
            route_dist += graph.distances.search_key((route[v], route[v + 1]))

    return route_dist


# Core algorithm of the program
# Parameters: Packages id list, start delivery time Returns: Final delivery time, Distance traveled
# This algorithm starts by sorting the packages with the nearest neighbor algorithm.
# The result is passed into the two-opt algorithm and that answer is the optimized route.
# The rest of the algorithm is used to timestamp packages ( deliver) and sum up the distance traveled.
# O(N^3) because of 2-opt being called
def deliver_packages(packages_load, start_time):
    # NN sort -> 2 opt
    r = nearest_neighbor_sort(generate_graph(packages_load), packages_load)
    optimized_route = two_opt(r)
    package_dist_list = ChainingHashTable()
    lp = 0
    index = 0
    d = datetime.datetime(2021, month=datetime.datetime.now().month, day=datetime.datetime.now().day,
                          hour=start_time.hour, minute=start_time.minute)
    d.replace(hour=start_time.hour, minute=start_time.minute)
    delivery_time = d
    final_time = d
    miles_traveled = optimized_route[0]
    # create package/dist id table
    for p in packages_load:
        for d in optimized_route[1]:
            if Distance.pkg_d_keys.search_key(p) == d:
                package_dist_list.insert(p, (p, d))
    # deliver packages- Timestamp and remove from package_dist_list
    for f, v in enumerate(optimized_route[1]):
        lp += 1
        if lp < len(optimized_route[1]):
            distance = Distance.distance_table.distances.search_key((v, optimized_route[1][f + 1]))
            travel_time = datetime.timedelta(minutes=Distance.time_to_travel(distance))
            delivery_time = delivery_time + travel_time
            if v != 0:
                for n, m in package_dist_list.get_values():
                    if m == v:
                        package_id = n
                        package_dist_list.remove_entry(package_id)
                        Packages.set_start_time(package_id, start_time)
                        Packages.set_delivery_timestamp(package_id, delivery_time)
                        final_time = delivery_time
                        index += 1
    return final_time, miles_traveled
