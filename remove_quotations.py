#when publishing data to a csv file, data might be wrapped within unwanted quotation marks 
#this is how to remove quotation marks 

import csv

def combine_quoted_elements(file_path1, file_path2):
    with open(file_path1, 'r') as file:
        reader = csv.reader(file)
        combined_rows = []

        for row in reader:
            combined_row = []
            inside_quotes = False
            combined_element = ''

            for element in row:
                if inside_quotes:
                    combined_element += ',' + element
                    if element.endswith('"'):
                        inside_quotes = False
                        combined_row.append(combined_element.strip('"'))
                        combined_element = ''
                elif element.startswith('"') and not element.endswith('"'):
                    inside_quotes = True
                    combined_element = element.strip('"')
                else:
                    combined_row.append(element)

            combined_rows.append(combined_row)

    with open(file_path2, 'w', newline='') as new_file:
        writer = csv.writer(new_file)
        writer.writerows(combined_rows)


file_path1 = ('yourfilepath1')
file_path2 = ('yourfilepath2')
combine_quoted_elements(file_path1, file_path2)
