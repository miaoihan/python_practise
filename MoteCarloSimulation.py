# coding:utf8
import random

NUM_OF_TRIALS = 10000000
numOfHits = 0.0	#落在圆内的个数
for  i in range(NUM_OF_TRIALS):
 	x = random.random()  * 2 - 1
 	y= random.random()  * 2 - 1
 	if x*x + y*y <=1:
 		numOfHits += 1
 
pi = 4 * numOfHits / NUM_OF_TRIALS
print('PI is', numOfHits,pi)

 