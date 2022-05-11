from utilities.sanitize import sanitize
from utilities.open_file import open_file
from utilities.generate_output import generate_output

def solution(inputFiles):
    data = []

    if inputFiles and len(inputFiles):
        for file in inputFiles:
            data += sanitize(open_file(file))
        
        return generate_output(data)