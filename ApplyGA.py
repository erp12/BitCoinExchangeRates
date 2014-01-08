### ApplyGA.py takes the input data for the network and
### the current current GA chromosome and creates the weighted
### inputs for the network.
import re

def run():
    with open('NormalizedData.txt') as f: #get training data as list of strings
        TrainingContent = f.readlines()

    with open('NormalizedTestingData.csv') as f: #get testing data as list of strings
        TestingContent = f.readlines()

    with open('currentChromosome.txt', 'r') as f: #get current chromosome as string
        chromosomeS = f.readline()

    #turn chromosome into list of ints
    chromosome = re.split(r'\t+', chromosomeS.rstrip('\t'))
    temp = 0
    for gene in chromosome:
        chromosome[temp] = float(gene)/100
        temp += 1

    #modify the training data
    weightedTrainingData = []
    for l in TrainingContent:   #line of orginonal file
        elements = re.split(r'\t+', l.rstrip('\t'))
        index = 0
        for e in elements:
            if index >0 and index <5:   #Leave first input and output untouched
                e = float(e)
                e = e * chromosome[index-1] # weight by chromosome
                e = str(e)
            weightedTrainingData.append(e)
            weightedTrainingData.append('\t')
            index += 1
        weightedTrainingData.append('\n')

    #turn new training data into one big string
    newTrainingFile = ''
    for e in weightedTrainingData:
        newTrainingFile = newTrainingFile + e

    #write new training data to file for emergent
    f = open('EmergentReadyTrainingData.txt', 'w')
    f.seek(0)
    f.write(newTrainingFile)
    f.truncate()
    f.close()
