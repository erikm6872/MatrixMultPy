#Erik McLaughlin
#11/10/2015

import matrixoperations as mo

def naive(n):
    a = mo.buildRandMatrix(n)
    b = mo.buildRandMatrix(n)
    
    mo.printMatrix(a, "A")
    mo.printMatrix(b, "B")
    
    c = matrixMult(a,b)
    
    mo.printMatrix(c, "C")
    
#Returns c, an nxn matrix that is the product of a and b
def matrixMult(a,b):    #Naive algorithm
    if mo.matricesSameSize(a,b):
        n = len(a)
        
        c = [[0 for x in range(n)] for x in range(n)] #Create new matrix, fill with 0s
        
        for i in range(n):          #Main algorithm loop
            for j in range(n):
                for k in range(n):
                    c[i][j] = c[i][j] + a[i][k] * b[k][j]
        return c
    else:
        print "Error: matrices are not the same size"
        print "Matrix A: %dx%d" % (len(a), len(a[0]))
        print "Matrix B: %dx%d" % (len(b), len(b[0]))
