import numpy as np
X1 = np.array([1, -2, 0, -1])
X2 = np.array([0, 1.5, -0.5, -1])
X3 = np.array([-1, 1, 0.5, -1])
X = np.array([X1, X2, X3])
W = np.array([1, -1, 0, 0.5])
print("W",1,  W) 
d = np.array([-1, -1, 1])
c = 0.1
epochs = 1
for i in range(epochs):
    for j in range(len(X)):
        net = np.dot(X[j], W)        
        if (net <= 0):
            op = -1
        elif net > 0:
            op = 1        
        error = d[j] - op       
        dW = c*error*X[j]
        W += dW
        print("W", j+2,  W)        
    print("\nW after ", i+1, " epochs ", W)    
print("Final W after ", epochs, "epochs:")
print(W) 
