import sys
NO_PATH=999

#Test case 1: Provided matrix
input_tr1=[
    [0, 7, NO_PATH, 8], 
    [NO_PATH, 0, 5, NO_PATH], 
    [NO_PATH, NO_PATH, 0, 2], 
    [NO_PATH, NO_PATH, NO_PATH, 0]
    ]

output_tr1=[
    [0, 7, 12, 8],
	[999, 0, 5, 7],
	[999, 999, 0, 2],
	[999, 999, 999, 0]
    ]

#Test case 2: More than 4 vertices

input_tr2=[
    [0, 7, NO_PATH, 8, 0], 
    [NO_PATH, 0, 5, NO_PATH, 0], 
    [NO_PATH, NO_PATH, 0, 2, 0], 
    [NO_PATH, NO_PATH, NO_PATH, 0, 0]
    ]

output_tr2=[
    [0, 7, 12, 8, 0],
    [NO_PATH, 0, 5, 7, 0],
    [NO_PATH, NO_PATH, 0, 2, 0],
    [NO_PATH, NO_PATH, NO_PATH, 0, 0]
    ]

#Test case 3: With negative value in vertics

input_tr3=[
    [0, -7, NO_PATH, -8], 
    [NO_PATH, 0, -5, NO_PATH], 
    [NO_PATH, NO_PATH, 0, -2], 
    [-2, NO_PATH, NO_PATH, 0]
    ]

output_tr3=[
    [-40, -127, -212, -294],
	[959, 0, -5, -7],
	[-24, -111, -392, -670],
	[-42, -129, -606, -2552]
    ]
	
#Test case 4: Matrix with 2 vertices

input_tr4=[
    [0, 7], 
    [NO_PATH, 0]
    ]

output_tr4=[
    [0, 7],
    [NO_PATH, 0]
    ]