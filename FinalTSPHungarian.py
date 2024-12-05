import pandas as pd
import requests
import folium
import networkx as nx
import random
import math
import numpy as np
from queue import PriorityQueue 
import heapq
from math import radians, sin, cos, sqrt, atan2
import queue

def findZero(matrix):
    n = matrix.shape[1]
    coordinates = []
    for row in range(n):
        for col in range(n):
            if matrix[row, col] == 0:
                coordinates.append((row, col))

    return coordinates

def findPenalties(matrix, coordinates):
    penaltyDict = {}

    n = matrix.shape[1]

    for (row, col) in coordinates:
        
        if np.isinf(matrix[row, :]).all() or np.isinf(matrix[:, col]).all():
            continue
         # find penalty in row

        minRow = float('inf')
        for j in range(n):
            if j != col and not np.isinf(matrix[row, j]):
                minRow = min(minRow, matrix[row, j])

        minCol = float('inf')
        for i in range(n):
            if i != row and not np.isinf(matrix[i, col]):
                minCol = min(minCol, matrix[i, col])
        
        penaltyDict[(row, col)] = float(minRow + minCol)
    
    sortedPenalties = sorted(penaltyDict.items(), key=lambda x: x[1], reverse=True)
    sortedPenaltiesDict = dict(sortedPenalties)
    return sortedPenaltiesDict
         
def markMaxPenalties(penaltyDict, matrix, path):
    n = matrix.shape[1]
    coords = []

    for (row, col), penalty in penaltyDict.items():
        if matrix[row, col] == np.inf and (col, row) in coords:
            continue

        if (col, row) not in coords and (row, col) not in coords and penalty != 0:
            if matrix[row, col] != np.inf:
                coords.append((row, col))
                matrix[row, col] - np.inf
                matrix[row, :] = np.inf
                matrix[:, col] = np.inf

    return matrix, coords

def findPath(coords):
    adj_list = {}
    
    for x, y in coords:
        if x not in adj_list:
            adj_list[x] = []
        adj_list[x].append(y)

    all_paths = []

    visited = set()

    def dfs(node, path):
        path.append(node)
        visited.add(node)

        if node in adj_list:
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, path)

        
    for startNode in adj_list.keys():
        if startNode not in visited:
            path = []
            dfs(startNode, path)
            all_paths.append(path)


    return all_paths


def findClosingLinks(path):
    copy = list(path)
    closingLinks = []
    for i in range(len(copy)):
        x = path[i][0]
        y = path[i][len(path[i]) - 1]
        closingLinks.append((x, y))

    return closingLinks

def changeMatrix(matrix, closingLinks, realMatrix):

    for i,_ in closingLinks:
        for _, j in closingLinks:
            matrix[j, i] = realMatrix[j, i]

    for i, j in closingLinks:
        matrix[j, i] = np.inf

    return matrix

def reduceMatrix(matrix):
    n = matrix.shape[0]

    for i in range(n):
        if not np.all(np.isinf(matrix[i, :])):
            minRowValue = np.min([matrix[i, j] for j in range(n) if not np.isinf(matrix[i, j])])
            for j in range(n):
                if not np.isinf(matrix[i, j]):
                    matrix[i, j] -= minRowValue

    for j in range(n):
        if not np.all(np.isinf(matrix[:, j])): 
            minColValue = np.min([matrix[i, j] for i in range(n) if not np.isinf(matrix[i, j])])
            for i in range(n):
                if not np.isinf(matrix[i, j]):
                    matrix[i, j] -= minColValue

    return matrix

def isComplete(matrix):
    n = matrix.shape[0]
    count = 0
    num = 0
    coords = []
    for i in range(n):
        for j in range(n):
            if matrix[i, j] != np.inf and matrix[i, j] != 0:
                count += 1
                coords.append([i, j])
    if count <= 1:
        return coords, True
    else:
        return -1,  False


def eulerianCycle(path, startingPoint):

    isComplete = False
    cycle = [i for i in path[0]]

    while not isComplete:
        for subpath in path:
            if subpath[0] == cycle[-1]:
                for x in subpath:
                    cycle.append(x)
        if len(cycle) > 1 and cycle[0] == cycle[-1]:
            isComplete = True
    
    i = 0
    while i < len(cycle) - 1:
        if cycle[i] == cycle[i + 1]:
            cycle.pop(i + 1)
        else:
            i += 1

    eulerianPath = []
    startIndex = 0
    for i in range(len(cycle)):
        if cycle[i] == startingPoint:
            eulerianPath.append(cycle[i])
            startIndex = i
            break
    
    index = startIndex + 1
    while len(eulerianPath) != len(cycle):
        if index == len(cycle) - 1:
            index = 0
        else:
            eulerianPath.append(cycle[index])
            index += 1
    
    
    return eulerianPath

def findTSPCost(eulerianPath):
    cost = 0

    for i in range(len(eulerianPath) - 1):
        cost += matrix[eulerianPath[i]][eulerianPath[i + 1]]

    return cost

def hungarianAlgorithm(matrix, realMatrix):
    np.fill_diagonal(matrix, np.inf) 

    matrix = matrix - matrix.min(axis=1)[:, None]  
    matrix = matrix - matrix.min(axis=0) 

    complete = False

    n = matrix.shape[1]
    path = []  

    zeroCoordinates = findZero(matrix)
    penaltyDict = findPenalties(matrix, zeroCoordinates)

    matrix, coords = markMaxPenalties(penaltyDict, matrix, path)  
    path = findPath(coords)

    closingLinks = findClosingLinks(path)
    matrix = changeMatrix(matrix, closingLinks, realMatrix)

    while not complete:
        reduceMatrix(matrix)
        zeroCoordinates = findZero(matrix)

        penaltyDict = findPenalties(matrix, zeroCoordinates)
        matrix, coords = markMaxPenalties(penaltyDict, matrix, path) 

        secondPath = findPath(coords)
        path.extend(secondPath)

        num, complete = isComplete(matrix)
        path.extend(num)

    eulerianPath = eulerianCycle(path, 0)
    print(eulerianPath)
    cost = findTSPCost(eulerianPath)
    print(cost)


matrix = np.array([
    [0.0, 16689.40653781, 14083.27598754, 2426.84831266, 16898.38183468, 6115.07239525, 14144.87470024],
    [16689.40653781, 0.0, 4863.15642394, 15245.08771197, 1337.5399068, 10593.20591782, 9122.0731163],
    [14083.27598754, 4863.15642394, 0.0, 11676.15396277, 6166.79972577, 10466.5164726, 10458.26827118],
    [2426.84831266, 15245.08771197, 11676.15396277, 0.0, 16181.18388172, 5770.02231106, 15215.35583847],
    [16898.38183468, 1337.5399068, 6166.79972577, 16181.18388172, 0.0, 10899.62703627, 8499.70277879],
    [6115.07239525, 10593.20591782, 10466.5164726, 5770.02231106, 10899.62703627, 0.0, 18358.42168228],
    [14144.87470024, 9122.0731163, 10458.26827118, 15215.35583847, 8499.70277879, 18358.42168228, 0.0]
])

# matrix = np.array([
#     [0.0, 220.0, 418.0, 520.0, 568.0, 608.0, 600.0, 806.0, 644.0, 570.0],
#     [220.0, 0.0, 198.0, 308.0, 362.0, 388.0, 462.0, 586.0, 445.0, 462.0],
#     [418.0, 198.0, 0.0, 140.0, 200.0, 191.0, 410.0, 388.0, 290.0, 438.0],
#     [520.0, 308.0, 140.0, 0.0, 60.0, 130.0, 521.0, 304.0, 150.0, 357.0],
#     [568.0, 362.0, 200.0, 60.0, 0.0, 143.0, 573.0, 281.0, 90.0, 335.0],
#     [608.0, 388.0, 191.0, 130.0, 143.0, 0.0, 464.0, 197.0, 198.0, 477.0],
#     [600.0, 462.0, 410.0, 521.0, 573.0, 464.0, 0.0, 580.0, 653.0, 848.0],
#     [806.0, 586.0, 388.0, 304.0, 281.0, 197.0, 580.0, 0.0, 270.0, 590.0],
#     [644.0, 445.0, 290.0, 150.0, 90.0, 198.0, 653.0, 270.0, 0.0, 320.0],
#     [570.0, 462.0, 438.0, 357.0, 335.0, 477.0, 848.0, 590.0, 320.0, 0.0]
# ])

copyMatrix = matrix

hungarianAlgorithm(copyMatrix, matrix)