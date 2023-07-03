import csv

#converting csv to string 
def csv_to_string(file_path1):
    with open(file_path1, 'r') as file:
        csv_data = file.read()
    return csv_data

file_path1 = ('filepath1')
csv_string = csv_to_string(file_path1)


#converting string to csv
def string_to_csv(csv_string, file_path2):
    # Split the string into lines
    lines = csv_string.split('\n')

    # Remove any empty lines
    lines = [line for line in lines if line.strip()]

    # Open the file in write mode
    with open(file_path2, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write each line as a CSV row
        for line in lines:
            row = line.split(',')
            writer.writerow(row)


file_path2 = ('filepath2')
string_to_csv(csv_string, file_path2)
