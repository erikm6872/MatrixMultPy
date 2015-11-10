#Erik McLaughlin
#11/10/2015

import matrixoperations as mo

def main(n):
    a = mo.buildRandMatrix(n)
    b = mo.buildRandMatrix(n)
    
    mo.printMatrix(a, "A")
    mo.printMatrix(b, "B")
    
    c = [[0 for x in range(n)] for x in range(n)]
    
    c = dcmm(c,a,b)
    mo.printMatrix(c, "C")
    #print "len(a) = %d" % len(a)
    #print "len(b) = %d" % len(b)
    #print "len(c) = %d" % len(c)
        
#Returns c, an nxn matrix that is the product of a and b
def dcmm(c,a,b):    
    if mo.matricesSameSize(a,b): #Check to make sure matrices are both nxn
        n = len(a)
        
        c = [[0 for x in range(n)] for x in range(n)]
        
        if n == 1:
            c[0][0] = a[0][0] * b[0][0]
        
        else:
            a11 = mo.subMatrix(a, 1, 1)
            a12 = mo.subMatrix(a, 1, 2)
            a21 = mo.subMatrix(a, 2, 1)
            a22 = mo.subMatrix(a, 2, 2)
            
            b11 = mo.subMatrix(b, 1, 1)
            b12 = mo.subMatrix(b, 1, 2)
            b21 = mo.subMatrix(b, 2, 1)
            b22 = mo.subMatrix(b, 2, 2)
            
            c11 = mo.subMatrix(c, 1, 1)
            c12 = mo.subMatrix(c, 1, 2)
            c21 = mo.subMatrix(c, 2, 1)
            c22 = mo.subMatrix(c, 2, 2)
            
            c11 = dcmm(c11, a11, b11)
            c12 = dcmm(c12, a11, b12)
            c21 = dcmm(c21, a21, b11)
            c22 = dcmm(c22, a21, b12)
            
            t = [[0 for x in range(n)] for x in range(n)]
            t11 = mo.subMatrix(t, 1, 1)
            t12 = mo.subMatrix(t, 1, 2)
            t21 = mo.subMatrix(t, 2, 1)
            t22 = mo.subMatrix(t, 2, 2)
            
            t11 = dcmm(t11, a12, b21)
            t12 = dcmm(t12, a12, b22)
            t21 = dcmm(t21, a22, b21)
            t22 = dcmm(t22, a22, b22)
            
            c = mo.recombineSubMatrices(c11,c12,c21,c22)
            t = mo.recombineSubMatrices(t11,t12,t21,t22)
            
            for i in range(len(c)):
                for j in range(len(c)):
                    c[i][j] = c[i][j] + t[i][j]

        return c
 

    
    
main(4) #Call main() with matrix size
        #Only works with matrices of size 2^n for some reason
