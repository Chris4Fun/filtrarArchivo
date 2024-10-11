import os
import re
from datetime import datetime

def main():
    analyzer()
    
def analyzer():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    nombre_archivo = f"DMS_PROD_{timestamp}.txt"

    # Regex patterns to match the lines
    event_pattern = re.compile(r'EVENT CATEGORY:\s*(.*)')  # Added capturing group
    locker_pattern = re.compile(r'.*LOCKER')
    date_pattern = re.compile(r'(DATE.*)')

    event_match = None
    date_match = None

    with open(nombre_archivo, "w") as outputFile:
        with open('datos/arch1_08.txt', "r") as inputFile:
            line = inputFile.readline()
            while line:
                # Capture EVENT CATEGORY
                event_result = event_pattern.match(line)
                if event_result:
                    event_match = event_result.group(1)
                
                # Capture DATE
                date_result = date_pattern.match(line)
                if date_result:
                    date_match = date_result.group(1)

                # If LOCKER is found, write the saved EVENT CATEGORY and DATE
                if locker_pattern.match(line) and event_match and date_match:
                    outputFile.write(f"{event_match} {date_match} {line}")
                    
                line = inputFile.readline()

if __name__ == "__main__":
    main()
