import numpy as np,sys
import Particle as pso,PSOLogger
import CalcSwarmsMapper as mapper


def calcPSOReducer():
    index = 1;
    #bestSwarm = pso.Particle("0;0;0;0;0;0;0;10000000000000;0;0;0");
    PSOLogger.info("calcPSO reducer method is started...")
    swarmArray = []
    for line in sys.stdin:
        line = line.replace("1\t","")
        PSOLogger.info("===>line is\n%s"%(line))
        swarm = pso.Particle(line)
        
        if index == 1:
           bestSwarm = swarm
           index = 0
        PSOLogger.info("swarm.persBestVal = %s and bestSwarm.persBestVal=%s"%(swarm.persBestVal, bestSwarm.persBestVal))
        
        if swarm.persBestVal < bestSwarm.persBestVal:
            bestSwarm = swarm;
            #swarm.globalBestPos = bestSwarm.particlePosition
            #swarm.globalBestVal = bestSwarm.fitness
        swarmArray.append(swarm)
        '''
        swarm.updatePos();
        swarm.fitnessEval(mapper.fitnessFunc);
        swarm.updateVelocity();
        print swarm.strRepr()
        '''
    for newSwarm in swarmArray:
       newSwarm.globalBestPos = bestSwarm.particlePosition
       newSwarm.globalBestVal = bestSwarm.fitness
       newSwarm.updatePos();
       newSwarm.fitnessEval(mapper.fitnessFunc);
       newSwarm.updateVelocity();
       print newSwarm.strRepr()

if __name__ == "__main__": 
   calcPSOReducer()