import numpy as np
f_list= [[1,1],[1,-1]]
X=np.array(f_list)
inv_X = np.linalg.inv(X)
print(inv_X)
Z = np.array([100, 3])
y = np.linalg.inv(X).dot(Z)
print(y)
