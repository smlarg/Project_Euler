"""
copied from 83

"""
test_matrix = [ [131, 673, 234, 103,  18],
                [201,  96, 342, 965, 150],
                [630, 803, 746, 422, 111],
                [537, 699, 497, 121, 956],
                [805, 732, 524,  37, 331] ]

import csv
with open('p081_matrix.txt', 'r') as matrix_file:
    csv_reader = csv.reader(matrix_file)
    matrix = [ [int(a) for a in line] for line in csv_reader]

big = sum([a for line in matrix for a in line])
size = 80

#size = 5
#matrix = test_matrix

path_costs = [ [ big ]*size for _ in range(size) ]
path_costs[0][0] = 0


def visit_node_neighbors(i,j):
    node_increment = matrix[i][j]
    node_path_cost = path_costs[i][j]
    node_value = node_path_cost + node_increment
    queue = []
    # if i !=0:
    #     if path_costs[i-1][j] > node_value:
    #         path_costs[i-1][j] = node_value
    #         queue.append((i-1,j))
    if i !=size - 1:
        if path_costs[i+1][j] > node_value:
            path_costs[i+1][j] = node_value
            queue.append((i+1,j))
    #if j !=0:
    #    if path_costs[i][j-1] > node_value:
    #        path_costs[i][j-1] = node_value
    #        queue.append((i,j-1))
    if j !=size - 1:
        if path_costs[i][j+1] > node_value:
            path_costs[i][j+1] = node_value
            queue.append((i,j+1))
    return queue

queue = [(0,0)]

while queue:
    next_gen = []
    for node in queue:
        new_nodes = visit_node_neighbors(*node)
        for new_node in new_nodes:
            next_gen.append(new_node)
    queue = next_gen.copy()

print( path_costs[size-1][size-1] + matrix[size-1][size-1] )
