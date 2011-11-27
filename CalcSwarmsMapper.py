import numpy as np,sys
import Particle as pso
import PSOLogger

def fitnessFunc(swarmPos):
    x = swarmPos[0];
    y = swarmPos[1];
    val = np.power((x - 15),2) + np.power((y - 20),2); 
    return val;

def calcPSOMapper():
    for line in sys.stdin:
        PSOLogger.info("calcPSO Mapper called")
        swarm = pso.Particle(line)
        #swarm.updatePos();
        #swarm.fitnessEval(fitnessFunc);
        #swarm.updateVelocity();
        print "1\t",swarm.strRepr()

        
if __name__ == "__main__": 
   calcPSOMapper()