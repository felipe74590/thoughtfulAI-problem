
##automation process
#function to read from csv
#function sorting function
    #remember to return error for invalid data, missing values or wrong types
#function to process/analyze data
#function to display

import re

def sort(width, height, length, mass)-> str:
    """
    Takes dimensions of a packages and returns the size classification.
    """
    size = "STANDARD"
    if mass >= 20:
        size = "SPECIAL"

    volume = width * height * length
    if  (width >= 150 or height >= 150 or length >= 150) or volume >= 1000000:
        if size == "SPECIAL":
            return "REJECTED"
        else:
            size = "SPECIAL"

    return size


def read_from_csv(path):
    "Takes path of csv file locations, returns list of data."
    data = []
    
    with open(path, mode='r') as file:
        for line in file:
            this_line = line.split(',')
            data.append(this_line)
    
    return data


def clean_data() -> list:
    """
    Cleans data by removing title lines, lines with missing dimensions or invalid values,
    and adds the size classification.
    """
    metrics = read_from_csv(path="sample_data.csv")
    valid_metrics = []
    
    for line in metrics:
        """Loop through each row of data and determine weather it has the required 4 dimensions, if they are not None,
        and if they can be converted to integers.
        Once the valid rows are identified, send them through the sort function to categorize the package.
        """
        valid = True

        if len(line) != 4:
            continue

        for index, metric in enumerate(line):
            clean_metric = metric.strip().strip('"').strip()
            clean_metric = re.sub(r'[^0-9]-', '', clean_metric)
            line[index] = clean_metric
            if not clean_metric.isdigit():
                valid = False

                print("Error this row contains invalid dimensions or title:", line)
                break

        if valid:
            width, height, length, mass = int(line[0]),int(line[1]),int(line[2]),int(line[3])
            size = sort(width, height, length, mass)

            valid_metrics.append([width, height, length, mass, size])

    print(valid_metrics)     
    
    return valid_metrics
   
        



if __name__ == "__main__":
    print(clean_data())