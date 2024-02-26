import sqlite3

# Connect to a database (creates if doesn't exist)
conn = sqlite3.connect('petur.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS vinna
               (date text, hedd text, erindi text)''')

# Insert a row of data
cursor.execute("INSERT INTO vinna VALUES ('2024-20-02', 'Fyrsta glós', 'Bý til sqlite python og fíla það vel!')")

# Save (commit) the changes
conn.commit()

# Query the database
cursor.execute("SELECT * FROM vinna")
print(cursor.fetchall())

# Close the connection
conn.close()