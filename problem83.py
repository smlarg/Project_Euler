"""
57ms

bou. ya. cha.

I wrote this with one thing to fix ( copy( thing) instead of thing.copy())
I am happy with this result
"""

"""
This is literally just Dijkstra’s algorithm
Which is great, that's exactly what I want to be asked


Wait. Actually, I feel like just doing a breadth-first search will be sufficient, and easier to implement?
just keep a(n unordered) queue of the frontier

"""
test_matrix = [ [131, 673, 234, 103,  18],
                [201,  96, 342, 965, 150],
                [630, 803, 746, 422, 111],
                [537, 699, 497, 121, 956],
                [805, 732, 524,  37, 331] ]

import csv
with open('p083_matrix.txt', 'r') as matrix_file:
    csv_reader = csv.reader(matrix_file)
    matrix = [ [int(a) for a in line] for line in csv_reader]

# holy crap that worked. nice.

big = sum([a for line in matrix for a in line])
size = 80

# not sure what standard will me least confusing for which edge is currently the best
# oh wait! The problem doesn't ask the path, just its value.
# great, that really simplfies things
#weights_and_directions = [ [[big,'neither up nor down']]*80 for _ in range(80) ]
path_costs = [ [ big ]*size for _ in range(size) ]
path_costs[0][0] = 0


def visit_node_neighbors(i,j):
    node_increment = matrix[i][j]
    node_path_cost = path_costs[i][j]
    node_value = node_path_cost + node_increment
    queue = []
    if i !=0:
        if path_costs[i-1][j] > node_value:
            path_costs[i-1][j] = node_value
            queue.append((i-1,j))
    if i !=size - 1:
        if path_costs[i+1][j] > node_value:
            path_costs[i+1][j] = node_value
            queue.append((i+1,j))
    if j !=0:
        if path_costs[i][j-1] > node_value:
            path_costs[i][j-1] = node_value
            queue.append((i,j-1))
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

# now do I need to add the last node? I think so
# (this really means my convention is bad; but whatever)
print( path_costs[size-1][size-1] + matrix[size-1][size-1] )


"""
# technically this is closer to Djikstra, as it has a min search; but in this case it's much slower
# searching just a queue would of course be a compromise, but I bet it's still slower
# (The Official Algorithms way would be a Fibonacci heap; but that's not happening)

import numpy as np

import csv
with open('p083_matrix.txt', 'r') as matrix_file:
    csv_reader = csv.reader(matrix_file)
    matrix = [ [int(a) for a in line] for line in csv_reader]

size = len(matrix)

test_matrix = [ [131, 673, 234, 103,  18],
                [201,  96, 342, 965, 150],
                [630, 803, 746, 422, 111],
                [537, 699, 497, 121, 956],
                [805, 732, 524,  37, 331] ]

#matrix = test_matrix
#size = 5

big = sum([a for line in matrix for a in line])

path_costs = np.full((size,size), big)
frontier_mask = np.full((size,size), big)


def visit_node_neighbors(i,j):
    node_value = path_costs[i][j]
    if i !=0:
        if path_costs[i-1][j] > node_value + matrix[i-1][j]:
            path_costs[i-1][j] = node_value + matrix[i-1][j]
            frontier_mask[i-1][j] = node_value + matrix[i-1][j]
    if i !=size - 1:
        if path_costs[i+1][j] > node_value + matrix[i+1][j]:
            path_costs[i+1][j] = node_value + matrix[i+1][j]
            frontier_mask[i+1][j] = node_value + matrix[i+1][j]
    if j !=0:
        if path_costs[i][j-1] > node_value + matrix[i][j-1]:
            path_costs[i][j-1] = node_value + matrix[i][j-1]
            frontier_mask[i][j-1] = node_value + matrix[i][j-1]
    if j !=size - 1:
        if path_costs[i][j+1] > node_value + matrix[i][j+1]:
            path_costs[i][j+1] = node_value + matrix[i][j+1]
            frontier_mask[i][j+1] = node_value + matrix[i][j+1]
    return


path_costs[0][0] = matrix[0][0]
frontier_mask[0][0] = matrix[0][0]

while (frontier_mask.max() != 2*big or frontier_mask.min() != 2*big):
    ni = np.unravel_index(np.argmin(frontier_mask), path_costs.shape)
    frontier_mask[ni[0], ni[1]] = 2* big
    visit_node_neighbors (ni[0], ni[1])

print (path_costs[size-1,size-1])

"""