#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 00:27:12 2018

@author: amarjithv
"""
import sys
import random
import math

#calculate the euclidean distance between x and y
def Distance(x, y):
    S = 0
    for i in range(len(x)):
        S += math.pow(x[i]-y[i], 2)
 
    return math.sqrt(S)

def Update_Mean(n,mean,row):
    for i in range(len(mean)):
        m = mean[i]
        m = (m*(n-1)+row[i])/float(n)
        mean[i] = round(m, 3)
     
    return mean

# Classify datapoint to the mean with minimum distance
def Classify(means,row):
 
        
    minimum = sys.maxint
    ind = -1
 
    for i in range(len(means)):
 
        # Find distance from datapoint to mean
        dis = Distance(row, means[i])
 
        if (dis < minimum):
            minimum = dis
            ind = i
     
    return ind



# Read the file
f = open('points.txt', 'r')
lines = f.read().splitlines()
f.close()
 
data = []
 
for i in range(0, len(lines)):
    line = lines[i].split(' ')
    rowfeatures = []
 
    for j in range(len(line)):
        v = float(line[j])
        rowfeatures.append(v)
 
    data.append(rowfeatures)

k = int(raw_input("Enter the number of clusters:"))

n = len(data[0])
mini = [sys.maxsize for i in range(n)]
maxi = [-sys.maxsize -1 for i in range(n)]     
for row in data:
    for f in range(len(row)):
        if (row[f] < mini[f]):
            mini[f] = row[f]
             
        if (row[f] > maxi[f]):
            maxi[f] = row[f]
                
f = len(data[0]) # number of features
means = [[0 for i in range(f)] for j in range(k)]
     
for mean in means:
    for i in range(len(mean)):
 
        # Set value to a random float
        mean[i] = random.uniform(mini[i]+1, maxi[i]-1)
 
csize= [0 for i in range(len(means))]
 
# An array to hold the cluster a datapoint is in
b = [0 for i in range(len(data))]
 
# Calculate optimal value of means
for e in range(100000):
 
    # If no change of cluster occurs, stop
    nochange = True
    for i in range(len(data)):
        row = data[i]
        # Classify row into a cluster and update the corresponding means.
        ind = Classify(means,row)
 
        csize[ind] += 1;
        cs = csize[ind]
        means[ind] = Update_Mean(cs,means[ind],row)
 
        if(ind != b[i]):
            nochange = False
 
        b[i] = ind
 
        
    if (nochange):
        break
print(means)
p = open('clusters.txt', 'w')
p.write(''+str(means))
p.close
