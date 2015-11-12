def matrixMult(a,b):    #Naive algorithm
    if matricesSameSize(a,b):
        n = len(a)
        
        c = [[0 for x in range(n)] for x in range(n)] #Create new matrix, fill with 0s
        
        for i in range(n):          #Main algorithm loop
            for j in range(n):
                for k in range(n):
                    c[i][j] = c[i][j] + a[i][k] * b[k][j]
        return c
        
def matricesSameSize(a,b):
    if len(a) != len(b) or len(a) != len(a[0]) or len(a[0]) != len(b[0]):
        return False
    else:
        return True