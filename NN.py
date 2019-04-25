from random import random
from math import exp
import copy
import csv
import numpy as np

def loadCSV(fileName):
    data = np.loadtxt(fileName, dtype=float, delimiter=",")
    print(fileName, " loaded in successfuly")
    return data




X = np.array(([0.1, 0.1]), dtype=float)
X1 = np.array(([0.1,0.2]), dtype=float)
y = np.array(([1,0]), dtype=float)
y1 = np.array(([0,1]), dtype=float)
mX = np.array(([0.1, 0.1],[0.1,0.2]), dtype=float)
my = np.array(([1,0], [0,1]), dtype=float)
"""
W1 = np.array(([0.1, 0.1],[0.2, 0.1]), dtype=float)
W2 = np.array(([0.1, 0.1],[0.1, 0.2]), dtype=float)
"""
# scale units
"""
X = X/np.amax(X, axis=0) # maximum of X array
y = y/100 # max test score is 100
"""

class Neural_Network(object):
    def __init__(self):
        #parameters
        self.inputSize = 2
        self.outputSize = 2
        self.hiddenSize = 2

        #weights
        #W1 = input -> hidden layer weights
        #W2 =  hidden layer -> output weights
        #self.W1 = np.random.randn(self.inputSize, self.hiddenSize)
        # (3x2) weight matrix from input to hidden layer
        #self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # (3x1) weight matrix from hidden to output layer
        self.W1 = np.array(([0.1, 0.1],[0.2, 0.1]), dtype=float)
        self.W2 = np.array(([0.1, 0.1],[0.1, 0.2]), dtype=float)
        self.bias1 = np.array(([0.1,0.1]), dtype=float)
        self.bias2 = np.array(([0.1,0.1]), dtype=float)


    def findError(self, o):
        meanSquare1 = 0.5*(y[0] -  o[0])**2
        meanSquare2 =0.5*(y[1] -  o[1])**2
        return meanSquare1 + meanSquare2
        print(meanSquare1)
        print(meanSquare2)

    def forward(self, X):
        #forward propagation through our network
        self.z = np.dot(X, self.W1) + self.bias1# dot product of X (input) and first set of 3x2 weights
        self.z2 = self.sigmoid(self.z) # activation function
        self.z3 = np.dot(self.z2, self.W2)+ self.bias2 # dot product of hidden layer (z2) and second set of 3x1 weights
        #print("after second sum",self.z3)
        o = self.sigmoid(self.z3) # final activation function
        return o

    def sigmoid(self, s):
        # activation function
        return 1/(1+np.exp(-s))

    def sigmoidPrime(self, s):
        #derivative of sigmoid
        return s * (1 - s)

    def backward(self, X, y, o):
        # backward propagate through the network
        self.o_error = y - o # error in output
        self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error
        print("delta",self.o_delta)
        self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
        #print("how much hidden layer weights contributed",self.z2_error)
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

        self.W1 += X.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
        self.W2 += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights



    def backProp(self, X, y,o):
        self.o_error = y - o # error in output
        self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error
        print("delta",self.o_delta)
        print()
        print("outh1, outh2",self.z2)
        #self.z2 = self.z2[::-1]
        tmp = self.z2 * self.o_delta * -1
        self.errorToNode = np.append (tmp, self.z2[::-1] * self.o_delta * -1)
        print(self.errorToNode)
        print(self.W2)
        NN.miniBatch()
        """ Bias 1 weight updates """

        """ First Layer """

        """ Bias 2 weight updates """


    def miniBatch(self):
        print()
        print("miniBatch")
        print(self.errorToNode)
        #combinedError = (w11[0]*-1) + 0.07263347
        #print(combinedError)
        #newWeight = (n * combinedError) / 2
        #weight = old - new
        #print("new w5",newWeight)
        #return newWeight


"""
    def train(self,X,y):
        o = NN.forward(X)
        NN.backward(X,y,o)
"""
NN = Neural_Network()
m = 2
n = 0.1
resultForward = NN.forward(X)
print("forward feed results",resultForward)
meanSquare = NN.findError(resultForward)
print("mean squared error",meanSquare)
print()
NN.backProp(X,y,resultForward)
#NN.miniBatch(w5, w8,m, n )

#NN.backProp(X,y,resultForward,meanSquare)



"""
for i in range(3): # trains the NN 1,000 times
    NN.train(X, y)

print("Input: \n" + str(X))
print("Actual Output: \n" + str(y))
print("Predicted Output: \n" + str(NN.forward(X)))
print("Loss: \n" + str(np.mean(np.square(y - NN.forward(X))))) # mean sum squared loss
print()
"""
