def dcmm(c,a,b):    
    if matricesSameSize(a,b): #Check to make sure matrices are both nxn
        n = len(a)
        
        c = [[0 for x in range(n)] for x in range(n)] #Create new matrix for result of multiplication
        
        if n == 1:
            c[0][0] = a[0][0] * b[0][0]
        
        else:
            #Split a, b, and c into 4 submatrices 
            a11 = subMatrix(a, 1, 1)
            a12 = subMatrix(a, 1, 2)
            a21 = subMatrix(a, 2, 1)
            a22 = subMatrix(a, 2, 2)
            
            b11 = subMatrix(b, 1, 1)
            b12 = subMatrix(b, 1, 2)
            b21 = subMatrix(b, 2, 1)
            b22 = subMatrix(b, 2, 2)
            
            c11 = subMatrix(c, 1, 1)
            c12 = subMatrix(c, 1, 2)
            c21 = subMatrix(c, 2, 1)
            c22 = subMatrix(c, 2, 2)
            
            
            #Recursively perform multiplication
            c11 = dcmm(c11, a11, b11)
            c12 = dcmm(c12, a11, b12)
            c21 = dcmm(c21, a21, b11)
            c22 = dcmm(c22, a21, b12)
            
            t = [[0 for x in range(n)] for x in range(n)]
            
            #Split t into submatrices
            t11 = subMatrix(t, 1, 1)
            t12 = subMatrix(t, 1, 2)
            t21 = subMatrix(t, 2, 1)
            t22 = subMatrix(t, 2, 2)
            
            t11 = dcmm(t11, a12, b21)
            t12 = dcmm(t12, a12, b22)
            t21 = dcmm(t21, a22, b21)
            t22 = dcmm(t22, a22, b22)
            
            #Recombine all submatrices of c and t into original matrices
            c = recombineSubMatrices(c11,c12,c21,c22)
            t = recombineSubMatrices(t11,t12,t21,t22)
            
            for i in range(len(c)):
                for j in range(len(c)):
                    c[i][j] = c[i][j] + t[i][j]
        return c
        
def recombineSubMatrices(a,b,c,d):  #a = m11, b = m12, c = m21, d = m22
        n = len(a) * 2
        retM = [[0 for x in range(n)] for x in range(n)]
        for i in range(len(a)):
            for j in range(len(a)):
                retM[i][j] = a[i][j]    #Copy values from a -> upper left
            for k in range(len(a), n):
                retM[i][k] = b[i][k-len(a)] #Copy values from b -> upper right
        for l in range(len(a), n):
            for m in range(len(a)):
                retM[l][m] = c[l-len(a)][m] #c -> lower left
            for o in range(len(a), n):
                retM[l][o] = d[l-len(a)][o-len(a)]  #d -> lower right
        return retM
        
def matricesSameSize(a,b):
    if len(a) != len(b) or len(a) != len(a[0]) or len(a[0]) != len(b[0]):
        return False
    else:
        return True
        
def subMatrix(m,i,j):
    n = len(m)
    nP = n/2
    retM = [[0 for x in range(nP)] for x in range(nP)] #create empty matrix 1/4 the size of input
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