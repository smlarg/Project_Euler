"""
1.87s

surprised it's so long; I would have guessed 5x problem83, not 40, but oh well
 - I don't know why it's longer than 83, but it's long in general because this can be O(n^2) because I didn't use Dijkstra
 - no, it's 40x as long because we have to run it 80 times! I doubt using an unorder queue really matters, because the graph is
   so sparsely connected.

copied from 83, from 81

I did not do it in the morning in the end, but yes this was the buggiest one
is i left-right or j? this shouldn't be hard. but it always is.
"""
"""
ah, this is actually a bit different. I need a loop over starting nodes
  AND ENDING NODES! Mhnmm. Dammit.

I'll do this in the morning.

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
    #if j !=0:
    #    if path_costs[i][j-1] > node_value:
    #        path_costs[i][j-1] = node_value
    #        queue.append((i,j-1))
    if j !=size - 1:
        if path_costs[i][j+1] > node_value:
            path_costs[i][j+1] = node_value
            queue.append((i,j+1))
    return queue

a_list_I_dont_strictly_need = [big]*size

for i in range(size):
    path_costs = [ [ big ]*size for _ in range(size) ]
    path_costs[i][0] = 0
    queue = [(i,0)]
    
    while queue:
        next_gen = []
        for node in queue:
            new_nodes = visit_node_neighbors(*node)
            for new_node in new_nodes:
                next_gen.append(new_node)
        queue = next_gen.copy()
    
    for j in range(size):
        a_list_I_dont_strictly_need[i] = min(a_list_I_dont_strictly_need[i] ,path_costs[j][size-1] + matrix[j][size-1])

print(min( a_list_I_dont_strictly_need))
