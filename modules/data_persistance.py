import csv

def FromCSV(filename, list): #file name is the name of the CSV, list is what list csv is writing to
    try:
        with open(f"./csv/{filename}.csv", 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                list.append(row)
        return(list)
    except FileNotFoundError as err:
        print(f"Sorry the file '{filename}' could not be found: ", err)

def ToCSV(filename, list): #file name is the name of the CSV, list is what list is being written to the csv
    keys = list[0].keys()
    with open(f"./csv/{filename}.csv", 'w', newline = '')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list)