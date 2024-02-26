import csv

# Open the CSV file with the correct encoding
with open("BIN_ordalisti.csv", "r", newline='', encoding='utf-8') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
    # Initialize an empty set to store unique values
    unique_values = set()
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Check if the row has at least two columns
        if len(row) >= 2:
            # Add the value in the second column to the set
            unique_values.add(row[1])
    
    # Print the number of unique values in the second column
    print(len(unique_values))
