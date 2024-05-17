import os
import re
import json

def main():
    analyzer()
    
def analyzer():
    # nombre_archivo = "FILTRADO.txt"
    # with open(nombre_archivo, "w") as outputFile:

    # Regex used to match all of the comments
    pattern = re.compile(r'^%%%%%TRAILER: (\w+)')
    trdPattern = re.compile(r'\s*,EXTENDED = TRUE')
    matchSet = {}

    match = None 
    sndMatch = None 
    strMatch = None
    sndStrMatch = None
    trdStrMatch = "EXTENDED = TRUE"
    
    counter = 0
    counterTwo = 0
    # Opening file
    with open('datos/DMS.TXT', "r") as inputFile:
        line = inputFile.readline()
        while line:
            counter +=1
            if pattern.match(line):
                match = pattern.match(line)
                strMatch = match.group(1)
            trdMatch = trdPattern.match(line)

            if trdMatch:
                counterTwo +=1
                # matchSet.add()
                print("Match: " + strMatch + " " + trdStrMatch + " " + str(counter) + " " + str(counterTwo))
                
            line = inputFile.readline()

    # Add the input to the lex\
    



if __name__ == "__main__":
    main()
    
