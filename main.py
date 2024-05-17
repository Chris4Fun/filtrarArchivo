#!/usr/bin/env python

import os
import re
from datetime import datetime

def main():
    analyzer()
    
def analyzer():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    nombre_archivo = f"DMS_PROD_{timestamp}.txt"

    # Regex used to match all of the comments
    pattern = re.compile(r'^%%%%%TRAILER: (\w+)')
    trdPattern = re.compile(r'\s*,EXTENDED = TRUE')

    match = None 
    strMatch = None
    
    # Opening file
    with open(nombre_archivo, "w") as outputFile:
        with open('datos/DMS.TXT', "r") as inputFile:
            line = inputFile.readline()
            while line:
                if pattern.match(line):
                    match = pattern.match(line)
                    strMatch = match.group(1)
                trdMatch = trdPattern.match(line)

                if trdMatch:
                        outputFile.write(strMatch + " EXTENDED" + '\n')
                    
                line = inputFile.readline()



if __name__ == "__main__":
    main()
    
