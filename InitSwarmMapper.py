#!/usr/bin/env python
import sys
import numpy as np,scipy as sci

def createInitSwarms():
    for line in sys.stdin:
        #--- get Swarm Config Values
        line = line.strip()
        params = line.split()

        numOfVariables = np.int32(params[0])
        boundsMin = np.float32(params[1])
        boundsMax = np.float32(params[2])
        popSize = np.int64(params[3])
        iterSize = np.int64(params[4])

        '''
        swarm = (boundsMax-boundsMin) * np.random.rand(popSize,numOfVariables) + boundsMin;
        swarm = np.hstack((swarm,100000*np.ones((popSize,1)))) 
        np.savetxt(sys.stdout, swarm, "%15.5f", ";", "\n")
        '''
        #--- total random matrix size
        #--- CurrPos(x1,x2,...,xn) + Velocity(x1,x2,...,xn) + fitnes + persBestPos(x1,x2,...,xn)+ pBestValue 
        #--- globalBestPos(x1,x2,...,xn) + globalBestValue
        
        totalMatrixSize = numOfVariables + numOfVariables + 1 + numOfVariables + 1 + numOfVariables + 1;
        
        #swarm = (boundsMax-boundsMin) * np.random.rand(popSize,totalMatrixSize) + boundsMin;
        swarm = (boundsMax-boundsMin) * np.random.rand(popSize,numOfVariables) + boundsMin;
        swarm = np.hstack((swarm,np.zeros((popSize,numOfVariables))));
        swarm = np.hstack((swarm,1000000*np.ones((popSize,1))));
        swarm = np.hstack((swarm,np.zeros((popSize,numOfVariables))))
        swarm = np.hstack((swarm,1000000*np.ones((popSize,1))));
        swarm =  np.hstack((swarm,np.zeros((popSize,numOfVariables))));
        swarm = np.hstack((swarm,1000000*np.ones((popSize,1))));
        #swarm = (boundsMax-boundsMin) * swarm + boundsMin;
        np.savetxt(sys.stdout, swarm, "%15.5f", ";", "\n")

if __name__ == "__main__": 
   createInitSwarms()