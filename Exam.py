import math
import numpy as np


from numpy import tanh

print("Questiopn 2")
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

print(sigmoid(3 + 1 * tanh(2+ 2 -1 -6)))

print('Question 1 Manthan')

print(sigmoid(2+ 4 - 5 -3))



print("Questiopn 3")
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

print(sigmoid(4 -1 * tanh(2+2-1-6) + -1 * tanh(-2 + 4 -4 + 3)))


print("Questiopn 5")

import math
v0 = 3
vx = -2
wz = 4
xx = 2
w0 = 2
az = np.tanh(v0 + (vx * xx))
ss = (wz*az)+ w0
ay = 1 / (1 + math.exp(-ss))

qw = ( wz* (1-ay) * xx * (1+az) * (1-az) * (-1))
print(qw)

print("Question 0000")

import math
v0 = 3
vx = -2
wz = 6
xx = 2
w0 = 2
t = 3
az = np.tanh(v0 + (vx * xx))
ay = w0 + (wz*az)   #linear
# print(ay)
# print((1+az)*(1-az)*xx)
print((1+az) * (1-az) * wz * (ay-t) * xx)