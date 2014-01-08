'''
Created on Mar 7, 2013

@author: jaime
'''
import re
import numpy



if __name__ == '__main__':
    inputFileName  = raw_input("Enter name of input file     : ")
    if inputFileName == "":
        inputFileName = "WDBC.dat"
    outputFileName = raw_input("Enter name of for output file: ")
    if outputFileName == "":
        outputFileName = "newWDBC.dat"
    inputArray = numpy.loadtxt(inputFileName)
    # if your data is incomplete, you might need to use 
    # numpy.genfromtxt
    print "read", len(inputArray), "elements"
    print inputArray

    inputArray = inputArray - inputArray.min(axis=0)
    inputArray = inputArray/(inputArray.max(axis=0))
    numpy.savetxt(outputFileName, inputArray, newline="\n")


