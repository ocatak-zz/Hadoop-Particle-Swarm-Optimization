import logging
logger = logging.getLogger('ParticelSwarmOptimization')
def initLogger():
   
   hdlr = logging.FileHandler('C:\personal\Doktora\Research\CloudComputing\hadoop-0.20.2\pythonDev\ParticelSwarmOptimization.log')    
   formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
   hdlr.setFormatter(formatter)
   logger.addHandler(hdlr) 
   logger.setLevel(logging.ERROR)
   
def info(str):
   pass
   #initLogger();
   #logger.info(str);

def debug(str):
   pass
   #initLogger();
   #logger.debug(str);
   
def error(str):
   pass
   #initLogger();
   #logger.error(str);