import numpy as np
X1 = np.array([1, 0, 0, 1, 0, 0, 1, 1, 1]) #L
X2 = np.array([1, 0, 0, 1, 0, 0, 1, 1, 1]) #L
X3 = np.array([1, 1, 0, 1, 0, 0, 1, 1, 1]) #L
X4 = np.array([1, 0, 0, 1, 0, 0, 1, 1, 1]) #L
X5 = np.array([1, 0, 0, 1, 0, 1, 1, 1, 1]) 
X6 = np.array([1, 0, 1, 1, 1, 1, 1, 0, 1]) #M
X7 = np.array([1, 0, 1, 1, 1, 1, 1, 0, 1]) #M
X8 = np.array([1, 0, 1, 1, 1, 1, 1, 0, 1]) #M
X9 = np.array([1, 0, 1, 1, 1, 1, 1, 1, 1]) 
X10 = np.array([1, 1, 1, 1, 1, 1, 1, 0, 1])
X = np.array([X1, X2, X3, X4, X5, X6, X7, X8, X9, X10])
W = np.array([1, 1.5, 2, 0.5,0.75,1.5,2,-1,2])
d = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
c = 1
epochs = 3
for i in range(epochs):
    print(f"\nIteration {i + 1}")
    for j in range(len(X)):
        net = np.dot(X[j], W)
        if net <= 0:
            op = 0
        elif net > 0:
            op = 1
        error = d[j] - op
        dW = c * error * X[j]
        W += dW
        print("W", j, W)
    print(f"W after {i + 1}epochs {W}")
print(f"\nFinal W after {epochs} epochs: ")
print(W)
def test(test_data, W):
    net = np.dot(test_data, W)
    if net <= 0:
        op = 'L'
    elif net > 0:
        op = 'M'
    return op
test_data1 = np.array([1, 0, 1, 1, 1, 1, 0, 0, 0])
test_data2 = np.array([0, 1, 0, 0, 1, 0, 0, 1, 1])
print(f"\nPrediction for test data: {test_data1} which is M and model gives : ", test(test_data1,W))
print(f"Prediction for test data: {test_data2} which is L and model gives : ", test(test_data2,W))
