import csv

path = "C:\\Users\\peturdaniel\\Downloads\\Flow_Network\\Today's Flow Rate Exceptions.csv"

# a function that reads the csv file and returns a list of dictionaries
def read_csv(path):
    with open(path, mode='r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# print out the headers (names for the columns) with their index number, so I can extract the columns I want
def get_headers_index(path):
    with open(path, mode='r') as f:
        # creates a CSV reader object
        csv_reader = csv.reader(f)
        # read the headers
        headers = next(csv_reader)
        # print the headers with their index numbers
        for index, header in enumerate(headers):
            print(f"Column {index}: {header}")

# prints the file as it is
def lesa_csv():
    with open(path, 'r') as f:
        for row in f:
            print(row)
