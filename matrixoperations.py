#Erik McLaughlin
#11/10/2015

import random

#Print the values in matrix m
def printMatrix(m, name):
    print "Matrix %s:" % name
    for x in range(len(m)):
        print m[x]
 
 
#Build a matrix of size n filled with random ints
def buildRandMatrix(n):
    retMatrix = [[0 for x in range(n)] for x in range(n)]
    for x in range(n):
        for y in range(n):
            retMatrix[x][y] = random.randint(0,10)
    return retMatrix
    
def recombineSubMatrices(a,b,c,d):
        n = len(a) * 2
        retM = [[0 for x in range(n)] for x in range(n)]
        for i in range(len(a)):
            for j in range(len(a)):
                retM[i][j] = a[i][j]
            for k in range(len(a), n):
                retM[i][k] = b[i][k-len(a)]
        for l in range(len(a), n):
            for m in range(len(a)):
                retM[l][m] = c[l-len(a)][m]
            for o in range(len(a), n):
                retM[l][o] = d[l-len(a)][o-len(a)]
        return retM
        
def matricesSameSize(a,b):
    if len(a) != len(b) or len(a) != len(a[0]) or len(a[0]) != len(b[0]):
        print "Error: matrices are not the same size"
        print "Matrix A: %dx%d" % (len(a), len(a[0]))
        print "Matrix B: %dx%d" % (len(b), len(b[0]))
        return False
    else:
        return True
        
def subMatrix(m,i,j):
    n = len(m)
    nP = n/2
    retM = [[0 for x in range(nP)] for x in range(nP)]
    if i == 1:
        for r in range(nP):
            if j == 1:
                for s in range(nP):
                    retM[r][s] = m[r][s]
            else:
                for s in range(nP,n):
                    retM[r][s-nP-1] = m[r][s]
    else:
        for r in range(nP,n):
            if j == 1:
                for s in range(nP):
                    retM[r-nP-1][s] = m[r][s]
            else:
                for s in range(nP,n):
                    retM[r-nP-1][s-nP-1] = m[r][s]
    return retM