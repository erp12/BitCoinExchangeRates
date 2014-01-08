from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import DBAdapters


# this is the evaluation (aka fitness) function
# that determines how good an element is.
def eval_func(chromosome):
   score = 0.0
   # iterate over the chromosome
   for value in chromosome:
      if value==0:
         score += 1
   return score

# this next line defines each element as having 200 integers.
genome = G1DList.G1DList(200)
# the integers generated above will be between 1 and 10.
# if you want a different range, do something like this:
# genome.setParams(rangemin=-4, rangemax=16)

# this next line defines what we should use
# as our fitness function.
# in this case it's the function defined at the beggining of the file.
genome.evaluator.set(eval_func)

# this next line creates the genetic simulation.
# in this case the genetic simulation is called ga.
# ga now controls/defines the genetic run. 
# You can now access different aspects of the genetic run
# thorugh ga.
ga = GSimpleGA.GSimpleGA(genome)

# see the end of this file to read what these next two lines do
sqlite_adapter = DBAdapters.DBSQLite(identify="ex1", resetDB=True)
ga.setDBAdapter(sqlite_adapter)

# the next line starts the evolutionary process.
# the process will run, as a default, for 100 generations.
# if you want to change the number of generations the evolution runs for,
# use something like ga.setGenerations(500).
# This run will generate reports every 10 generations.
ga.evolve(freq_stats=10)

# some other defaults (from http://pyevolve.sourceforge.net/getstarted.html):
# By default, the GA will evolve for 100 generations 
# with a population size of 80 individuals, 
# it will use the mutation rate of 2% 
# and a crossover rate of 80%, 
#the default selector is the Ranking Selection (Selectors.GRankSelector()) method.

# how to change those defaults (from http://pyevolve.sourceforge.net/module_gsimplega.html):
# number of generations: ga.setGenerations(120)
# population size: ga.setPopulationSize(size)
# mutation rate: ga.setMutationRate(rate) . The rate is a number between 0.0 and 1.0
# crossover rate: ga.setCrossoverRate(rate) The rate is a number between 0.0 and 1.0
# selection method: ga.selector.set(Selectors.GRouletteWheel)
#	the list of selection methods is at http://pyevolve.sourceforge.net/0_6rc1/module_selectors.html

# once the run finishes, we print the best element evolved.
print ga.bestIndividual()


# pyevolve also has a great library of plotting functions.
# Documentation is available at http://pyevolve.sourceforge.net/graphs.html
# To use this package and generate some graphs, 
# you have to:
# 	attach a database to your run, by doing something like 
#	sqlite_adapter = DBAdapters.DBSQLite(identify="ex1")
#	ga.setDBAdapter(sqlite_adapter)
# Those commands will dump a bunch of statistics to a file called pyevolve.db
# You then run the graphs generation package by running "pyevolve_graph.py -i ex1 -1"
