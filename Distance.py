import csv
import math
import Packages
from WeightedGraph import *

# Reading distance addresses file and parsing data
# O(N)
with open('./Data/Distance_addresses.csv') as csv_file:
    read_file = csv.reader(csv_file, delimiter=',')

    distance_table = WeightedGraph()
    dist_addresses = []
    pkg_d_keys = ChainingHashTable()

    for row in read_file:
        index = int(row[0])
        name = row[1]
        address = row[2]
        zipCode = row[3]
        dist_addresses.append(address)

# Reading distance table file and parsing data
# O(N)
with open('./Data/DistanceTable.csv') as csv_file2:
    read_file2 = csv.reader(csv_file2, delimiter=',')

    for rows in read_file2:
        start_loc = rows.index("0.0")
        i = 0
        for row in rows:
            if row != '':
                distance_table.add_vertex(start_loc)
                distance_table.add_vertex(i)
                distance_table.add_edge(start_loc, i, row)
            i += 1

    # return travel time rounded up to nearest minute
    # O(1)
    def time_to_travel(distance):
        time = math.ceil((distance / 18) * 60)
        return time

    # Mapping distance and package keys to one another
    # O(N^2)
    def compare_addresses():
        for p in range(len(Packages.pack_addresses)):
            for d in range(len(dist_addresses)):
                if dist_addresses[d].__contains__(Packages.pack_addresses[p]) or dist_addresses[d] == Packages.pack_addresses[p]:
                    pkg_d_keys.insert(p + 1, d)
