../bin/hadoop fs -rmr p1output/
../bin/hadoop fs -rmr p1outputTotal/
../bin/hadoop fs -rmr bestSwarm/
../bin/hadoop fs -rmr swarmsOut/

../bin/hadoop fs -rm SwarmParams.txt
../bin/hadoop fs -put SwarmParams.txt SwarmParams.txt

../bin/hadoop jar ../contrib/streaming/hadoop-0.20.2-streaming.jar -input SwarmParams.txt -output swarmsOut/iters1 -mapper "python c:/Personal/Doktora/Research/CloudComputing/hadoop-0.20.2/pythonDev/InitSwarmMapper.py" -reducer "python c:/Personal/Doktora/Research/CloudComputing/hadoop-0.20.2/pythonDev/InitSwarmReducer.py" -file c:/Personal/Doktora/Research/CloudComputing/hadoop-0.20.2/pythonDev/InitSwarmMapper.py -file c:/Personal/Doktora/Research/CloudComputing/hadoop-0.20.2/pythonDev/InitSwarmMapper.py #-jobconf mapred.reduce.tasks=8
for i in {1..100}
do
   infile="swarmsOut/iters$i"
   let j=$i+1
   outfile="swarmsOut/iters$j"
   echo "------"
   echo $infile
   echo $outfile
   ../bin/hadoop jar ../contrib/streaming/hadoop-0.20.2-streaming.jar -input ${infile} -output ${outfile} -mapper "python c:/Personal/Doktora/Research/CloudComputing/hadoop-0.20.2/pythonDev/CalcSwarmsMapper.py" -reducer "python c:/Personal/Doktora/Research/CloudComputing/hadoop-0.20.2/pythonDev/CalcSwarmsReducer.py" -file c:/Personal/Doktora/Research/CloudComputing/hadoop-0.20.2/pythonDev/CalcSwarmsMapper.py -file c:/Personal/Doktora/Research/CloudComputing/hadoop-0.20.2/pythonDev/CalcSwarmsReducer.py #-jobconf mapred.reduce.tasks=6
done