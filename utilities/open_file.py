#Returns an array of all lines per file
def open_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    return lines