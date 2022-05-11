from datetime import datetime

#Generates output
def generate_output(data):
    output = ""
    output += "\n" + "Output 1:" + "\n"
    output += "\n".join(sort_by_gender_and_last_name_asc(data))
    output += 2*"\n" + "Output 2:" + "\n"
    output += "\n".join(sort_by_birthdate_and_last_name_asc(data))
    output += 2*"\n" + "Output 3:" + "\n"
    output += "\n".join(sort_by_lastname_desc(data))
    return output

#Sorts data for the 3 output scenarios
def sort_by_gender_and_last_name_asc(data):
    data = sorted(data, key = lambda line: line.split()[0])
    data = sorted(data, key = lambda line: line.split()[2])
    return data

def sort_by_birthdate_and_last_name_asc(data):
    data = sorted(data, key = lambda line: line.split()[0])
    data = sorted(data, key = lambda line: datetime.strptime(line.split()[3], '%m/%d/%Y'))
    return data

def sort_by_lastname_desc(data):
    data = sorted(data, key = lambda line: line.split()[0], reverse = True)
    return data