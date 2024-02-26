import pandas as pd

pathMax = "C:\\Users\\peturdaniel\\Downloads\\Flow_Network\\Today's Flow Rate Exceptions - Max.csv"
pathMin = "C:\\Users\\peturdaniel\\Downloads\\Flow_Network\\Today's Flow Rate Exceptions - Min.csv"
pathMNo = "C:\\Users\\peturdaniel\\Downloads\\Flow_Network\\Today's Flow Rate Exceptions - No.csv"

# use the read_csv() function to read the csv file into a DataFrame
df = pd.read_csv(pathMax)

# Explore the DataFrame
#print(df.head())  # head(10)

# Access specific columns
column_site = df['Site ID']
column_grade = df['Grade']
column_flow_avg = df['Average Flow Rate in Period']

# Access specific rows using "iloc[]" method
row_index = 2
row_data = df.iloc[row_index]

selected_columns = df[['Grade', 'Average Flow Rate in Period']]
selected_columns = selected_columns[df['Site ID'] == '315']

print(selected_columns)

