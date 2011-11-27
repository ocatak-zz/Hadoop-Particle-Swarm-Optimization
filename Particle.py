import numpy as np
import string,PSOLogger

class Particle:
    corrFactor = 2;
    def __init__(self,pos):
        vals = np.array( [np.float(val) for val in pos.split(";")]);
        numOfVariables = (np.alen(vals)-3)/4;
        
        '''
        self.particlePosition = [np.float64(val) for val in vals[0].split(",")];
        self.velocity = [np.float64(val) for val in vals[1].split(",")];
        self.fitness = [np.float64(val) for val in vals[2].split(",")];
        self.persBestPos = [np.float64(val) for val in vals[3].split(",")];
        self.persBestVal = [np.float64(val) for val in vals[4].split(",")];
        self.globalBestPos = [np.float64(val) for val in vals[5].split(",")];
        self.globalBestVal = [np.float64(val) for val in vals[6].split(",")];
        '''
        index = 0
        self.particlePosition = vals[index:index+numOfVariables];
        index += numOfVariables
        self.velocity = vals[index:index+numOfVariables];
        index += numOfVariables
        self.fitness = vals[index:index+1];
        index += 1
        self.persBestPos = vals[index:index+numOfVariables];
        index += numOfVariables
        self.persBestVal = vals[index:index+1];
        index += 1
        self.globalBestPos = vals[index:index+numOfVariables];
        index += numOfVariables
        self.globalBestVal = vals[index:index+1];
    #--- update swarm position with velocity
    def updatePos(self):
        index = 0;
        for pos in self.particlePosition:
            self.particlePosition[index] += self.velocity[index]/1.3;
            index +=1;
    #--- calculate swarm fitness velocity
    def updateVelocity(self):
        index = 0;
        for vel in self.velocity:
            self.velocity[index] = np.random.rand()*self.velocity[index];
            self.velocity[index] += self.corrFactor*np.random.rand()*(self.persBestPos[index]-self.particlePosition[index]) 
            self.velocity[index] += self.corrFactor*np.random.rand()*(self.globalBestPos[index]-self.particlePosition[index]);
            index +=1;
    #--- fitness evaluation for swarm
    def fitnessEval(self,fitnessFunc):
        self.fitness = fitnessFunc(self.particlePosition) 
        if self.fitness < self.persBestVal:
            self.persBestPos = self.particlePosition
            self.persBestVal =  self.fitness
            
    def strRepr(self):
        res = ""
        for pos in self.particlePosition:
            res += np.str( pos )+ ";"
        for pos in self.velocity:
            res += np.str( pos )+ ";"
        res += np.str(self.fitness) + ";"
        for pos in self.persBestPos:
            res += np.str( pos )+ ";"
        res += np.str(self.persBestVal) + ";"
        for pos in self.globalBestPos:
            res += np.str( pos )+ ";"
        res += np.str(self.globalBestVal)+ ";"
        
        res = res.replace("[", "").replace("]","");
        #return res;
        return res[0:len(res)-2];
        
# test
if __name__ == "__main__":
    swarm = Particle("8.58739;27.30728;-27.29225;-18.17807;36.36847;-16.92002;-15.06649;25.14018; -35.27176; 0.26614; 5.56373");
    print swarm.particlePosition
    print swarm.velocity
    print swarm.fitness
    print swarm.persBestPos
    print swarm.persBestVal 
    print swarm.globalBestPos
    print swarm.globalBestVal
    print "-"*20
    print swarm.particlePosition
    print swarm.strRepr()