import sys
import itertools

# If there is no path between two nodes, the graph states INF. INF is defined below a large integer.
INF=999

# This algorithm will find the shortest route between each vertice in the below matrix
print("Initial graph is below: ")

graph=[
    [0, 7, INF, 8], 
    [INF, 0, 5, INF], 
    [INF, INF, 0, 2], 
    [INF, INF, INF, 0]
    ]

print(graph)

# MAX_LENGTH is set to the number of vertices in the graph as below
MAX_LENGTH=len(graph[0])

def floyd(distance): 
    for k,i,j in itertools.product(range(MAX_LENGTH),range(MAX_LENGTH),range(MAX_LENGTH)):
        if i==j:
            distance[i][j]=0 
            continue
        
        distance[i][j]= min(distance[i][j],distance[i][k]+distance[k][j]) 
    print(distance) 
import sys
import itertools

# If there is no path between two nodes, the graph states INF. INF is defined below a large integer.
INF=999

# This algorithm will find the shortest route between each vertice in the below matrix
print("Initial graph is below: ")

graph=[
    [0, 7, INF, 8], 
    [INF, 0, 5, INF], 
    [INF, INF, 0, 2], 
    [INF, INF, INF, 0]
    ]

print(graph)

# MAX_LENGTH is set to the number of vertices in the graph as below
MAX_LENGTH=len(graph[0])

def floyd(distance): 
    for k,i,j in itertools.product(range(MAX_LENGTH),range(MAX_LENGTH),range(MAX_LENGTH)):
        if i==j:
            distance[i][j]=0 
            continue
        
        distance[i][j]= min(distance[i][j],distance[i][k]+distance[k][j]) 
    print(distance) 
  
# Use below function to call shortest distance matrix
print("The following matrix shows the shortest distances between every pair of vertices")
floyd(graph)  
# Use below function to call shortest distance matrix
print("The following matrix shows the shortest distances between every pair of vertices")
floyd(graph)
