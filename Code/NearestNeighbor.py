import read_input
import timeit
import math 
import numpy as np
import plot
import time
import random

def closestNode(cities, current, unvisited):
    dmin = float("inf")
    closest = -1
    #print(unvisited)
    x = len(unvisited)
    for j in range(x):
        next = unvisited[j];
        cityX = cities[current][0] - cities[next][0]
        cityY = cities[current][1] - cities[next][1]
        distance = math.sqrt(cityX**2 + cityY**2)
        if distance < dmin :
            dmin = distance
            closest = next
    return closest, dmin
        

def algorithm(cities):

    unvisited =[]
    N = cities.shape[0]
    sum=0
    for i in range(0,N):
        unvisited.append(i);
    first = random.choice(unvisited)
    print(first)
    unvisited.remove(first)
    opt_path = [first]    
    while(len(unvisited) >= 1): 
        
        #print("length",len(unvisited))
        closest, dist = closestNode(cities, opt_path[-1], unvisited)
        opt_path.append(closest)
        unvisited.remove(closest)
        sum += dist

    ## return to the origin node
    closest, dist = closestNode(cities, opt_path[-1], [first])
    opt_path.append(closest)
    sum += dist              
    return opt_path, sum
    