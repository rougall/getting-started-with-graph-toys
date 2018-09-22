## Code to walk along all paths of a given length. Python 2.7
## Directed-graph structure given by dictionary class.
## Super-simple code, works for any depth, doesn't assume knowlegde of vertex degrees in advance, avoids creating adjacency matrix

# Directed-graph structure given by dictionary
mydict = {}
mydict[0]=[0,1,2,3]
mydict[1]=[0,1,2,3]
mydict[2]=[0,1,2,3]
mydict[3]=[3]

max_depth = 3 #this is the length of the paths we want
initial_vertex = 0 #this is the start point

#variables to track position
pointer = max_depth-1
ITER = [0]*max_depth
L_ITER = [0]*max_depth
carry = 1

#implement the walks; always reinitialising to start vertex
while pointer > -1:
    parent = initial_vertex
    depth = 0
    while depth < max_depth:
        set = mydict[parent] #possible next steps from parent
        l = len(set) #degree of vertex
        L_ITER[depth]=l-1
        index = ITER[depth] #ITER determines which next step
        child = set[index]
        parent = child #the child becomes the parent
        depth = depth + 1
    print ITER #gives the order of the path taken
    carry = 1
    pointer = max_depth-1 # this is also depth - 1
    while carry:
        if (ITER[pointer] < L_ITER[pointer]): #says we only have to back-track by one step
            ITER[pointer] = ITER[pointer] + 1 #the next index to use
            carry = 0
        else:
            ITER[pointer]=0
            pointer = pointer - 1 #says we have to back-track two-steps (at least)
            if pointer > -1:
                carry = 1
            else:
                carry = 0
