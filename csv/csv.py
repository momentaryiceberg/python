import csv

def create_txt_from_csv(csv_file, txt_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csv_input:
        reader = csv.reader(csv_input)
        
        # Assuming your CSV has a header row, skip it
        next(reader, None)
        
        with open(txt_file, 'w', encoding='utf-8') as txt_output:
            for row in reader:
                # Assuming column 4 is the index 3 (0-based) in the row
                value_from_column_4 = row[3]
                txt_output.write(value_from_column_4 + '\n')

# Replace 'input.csv' and 'output.txt' with your actual file names
create_txt_from_csv('input.csv', 'output.txt')
