import numpy as np

# two rows of A
payoffMatrix1 = np.array([[0.3, 0],[0.5, 0.1]])
A = payoffMatrix1
strategyProfile1 = np.array([0.4, 0.6])
x = strategyProfile1

# two columns of B
payoffMatrix2 = np.array([[0.3, 0],[0.5, 0.1]])
B = payoffMatrix2
strategyProfile2 = np.array([0.5, 0.5])
y = strategyProfile2

EVOLUTION_STEPS = 2

for step in range(EVOLUTION_STEPS):
    print("********* Step {} *********".format(step+1))
    print("x at step {}: {}".format(step+1, x))
    print("y at step {}: {}".format(step+1, y))

    Ay = np.sum(A*y[:, np.newaxis], axis=1)
    xTAy = np.transpose(x).dot(Ay)
    print("Ay at step {}: {}".format(step+1, Ay))
    print("xTAy at step {}: {}".format(step+1, xTAy))

    xDot = np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        xDot[i] = round(x[i] * (Ay[i]-xTAy),6)
        print("Population change for strategy {} of player {}: {}".format(i+1, 1, xDot[i]))
    
    xTB = np.sum(x*B, axis=1)
    xTBy = round(xTB.dot(y),6)
    print("xTB at step {}: {}".format(step+1, xTB))
    print("xTBy at step {}: {}".format(step+1, xTBy))

    yDot = np.zeros(A.shape[1])
    for i in range(A.shape[1]):
        yDot[i] = round(y[i] * (xTB[i]-xTBy), 6)
        print("Population change for strategy {} of player {}: {}".format(i+1, 2, yDot[i]))
    
    x = x + xDot
    print("Updated x for evolutionary step {}: {}".format(step+1, x))

    y = y + yDot
    print("Updated y for evolutionary step {}: {}\n".format(step+1, y))



