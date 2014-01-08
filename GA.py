from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import DBAdapters
import ApplyGA
import subprocess
import inspect, os, re

def get_network_error():
    with open('NetworkOutput.txt') as f: #get training data as list of strings
        networkOutput = f.readlines()
    s = networkOutput[len(networkOutput)-1]
    s = re.split(r',+', s.rstrip(','))
    s = float(s[3])
    s = (1-s)
    if s < 0:
        return 0
    else:
        return s*100

def eval_func(chromosome):
    score = 0.0

    #Write the chromosome
    f = open('currentChromosome.txt', 'w')  #Open the file with the current chromosome in it
    f.seek(0)                               #Go to the beginning of the file
    for v in chromosome:                    #For each value in the chromosome...
        f.write(str(v) + '\t')              #write a string and then '\t'
    f.truncate()                            #if there is extra text in file after that, get rid of it
    f.close()                               #close the file

    #Run ApplyGA.py to create the final data for emergent
    ApplyGA.run()
    
    #Get the error of the network
    loc = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) #location of this python file
    proj = loc+'\BitCoinPrediction.proj'                                            #add the project title to the end of loc
    ("emergent -nogui -ni -proj " + str(proj) + " batches=1 epoch=1 log_dir=. tag=test1") #call emergent 
    #^^^^^^^^^^^^^^I HOPE THIS DIRECTORY FINDING IS CROSS PLATFORM^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    score = get_network_error()
    return score

genome = G1DList.G1DList(5)
genome.setParams(rangemin=0, rangemax=200) #200 = weight twice as much as normal, 50 = half as much a normal (ApplyGA.py divides these by 100)
genome.evaluator.set(eval_func)
ga = GSimpleGA.GSimpleGA(genome)

sqlite_adapter = DBAdapters.DBSQLite(identify="ex1", resetDB=True)
ga.setDBAdapter(sqlite_adapter)

ga.evolve(freq_stats=10)

print ga.bestIndividual()
