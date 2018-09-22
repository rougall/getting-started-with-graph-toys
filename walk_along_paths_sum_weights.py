## Code to walk along paths of given length and sum weights. Python 2.7
## Directed-graph and weights structure given by dictionary class.
## Super-simple code, works for any depth, doesn't assume knowlegde of vertex degrees in advance, avoids creating adjacency matrix

# Directed-graph structure given by dictionary
graph = {}
graph['0']=['0','1','2']
graph['1']=['0','1','2']
graph['2']=['2']

# Weights likewise
weights = {}
weights['0,0'] = 1
weights['0,1'] = 2
weights['0,2'] = 3
weights['1,0'] = 2
weights['1,1'] = 3
weights['1,2'] = 4
weights['2,2'] = 5

#initial data
initial_vertex = '0'
max_depth = 3
weight_sum = 0


pointer = max_depth-1
ITER = [0]*max_depth
L_ITER = [0]*max_depth
carry = 1

while pointer > -1:
    weight_part = 1
    depth = 0
    parent = initial_vertex
    while depth < max_depth:
        set = graph[parent]
        l = len(set)
        L_ITER[depth]=l-1
        index = ITER[depth]
        child = set[index]
        edge = parent + ',' + child
        val = weights[edge]
        weight_part = weight_part*val #here we take the product along the path
        parent = child
        depth = depth + 1
    weight_sum = weight_sum + weight_part #here we take the sum of all paths
    carry = 1
    pointer = max_depth-1
    while carry:
        if (ITER[pointer] < L_ITER[pointer]):
            ITER[pointer] = ITER[pointer] + 1
            carry = 0
        else:
            ITER[pointer]=0
            pointer = pointer - 1
            if pointer > -1:
                carry = 1
            else:
                carry = 0
print weight_sum
