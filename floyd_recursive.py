import sys
import itertools

NO_PATH=999

graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]

MAX_LENGTH=len(graph[0])

#i - start_node
#j - end_node
#k - intermediate
#d - distance

def sol(i,j,k,d):

	if k < 0:
		return (d[i][j])
	return min(sol(i,j,k-1,d),
			   sol(i,k,k-1,d)+
			   sol(k,j,k-1,d)
			   )
				
def floyd(d):
	
	for i,j in itertools.product(range(MAX_LENGTH),range(MAX_LENGTH)):
		if i==j:
			d[i][j]=0
			continue
			
		d[i][j]=sol(i,j,MAX_LENGTH-1,d)
	return d
	
if __name__ == '__main__':
    print(floyd(graph))