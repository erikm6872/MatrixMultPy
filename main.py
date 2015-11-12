#Erik McLaughlin
#11/10/2015

import matrixoperations as mo
import divideandconquer as dc
import naive as n
import time

def main():
    minN = 8
    maxN = 32
    startTime = time.time()
    nTime = []
    dcTime = []
    for i in range(minN,maxN):
        n.naive(i)
        print 
        nTime.append(time.time() - startTime)
        startTime = time.time()
    for i in range(minN,maxN):
        dc.divideAndConquer(i)
        dcTime.append(time.time() - startTime)
        startTime = time.time()
    print "Naive algorithm times:"
    for i in range(minN,maxN):
        print "%f" % nTime[i-minN]
    print "Divide and Conquer algorithm times:"
    for i in range(minN,maxN):
        print "%f" % dcTime[i-minN]
    
main() 
