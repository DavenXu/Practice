import numpy as np 

matrix = np.array([[1, 2, 3], [10, 11, 12], [4, 5, 6], [7, 8, 9]])
maxRaw = sum(matrix[0])
index = 0

for i in range(matrix.shape[0]):
    if sum(matrix[i]) > maxRaw : 
        maxRaw = sum(matrix[i])
        index = i  
    else:
        maxRaw = maxRaw

print(maxRaw, index)
