#sanitizes and returns data per file
def sanitize(file):
    values = []
    middle_initial_index = 2

    for line in file:
        line_array = line.split(" ")
        line_array.pop(middle_initial_index)

        if line_array[1] == "|":
            line_array = sanitize_pipe_data(line, line_array, middle_initial_index)

        elif line_array[0][-1] == ",":
            line_array = sanitize_comma_data(line, line_array)

        line_array[3] = line_array[3].replace("-", "/")
        line_array[2] = "Female" if line_array[2] == "F" else "Male"
        values.append(flatten(line_array))
    return values

#swaps date and color fields for a single line
def swap_date_color(line_array): 
    line_array[-1], line_array[-2] = line_array[-2], line_array[-1]
    return line_array

#sanitizes by removing pipes, trailing spaces, middle initial and calls the swap function per line
def sanitize_pipe_data(line, line_array, middle_initial_index):
    line_array = line.split(" | ")
    line_array.pop(middle_initial_index)
    line_array = swap_date_color(line_array)
    return line_array

#sanitizes by removing commas, trailing spaces and calls the swap function per line
def sanitize_comma_data(line, line_array):
    line_array = line.split(", ")
    line_array = swap_date_color(line_array)
    return line_array

#takes an array and outputs flat text
def flatten(arr):
    return " ".join(arr)
