import sys
import itertools

NO_PATH=999

graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]

MAX_LENGTH=len(graph[0])

#k - intermediate
#i - start_node
#j - end_node

def floyd(distance): 
    for k,i,j in itertools.product(range(MAX_LENGTH),range(MAX_LENGTH),range(MAX_LENGTH)):
        if i==j:
            distance[i][j]=0 
            continue
        
        distance[i][j]= min(distance[i][j],distance[i][k]+distance[k][j]) 
    print (distance) 
 
floyd(graph)
