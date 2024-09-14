import csv

# Define the data
data = [
    ['Position', 'Level', 'Salary'],
    ['Business Analyst', '1', '45000'],
    ['Junior Consultant', '2', '50000'],
    ['Senior Consultant', '3', '60000'],
    ['Manager', '4', '80000'],
    ['Country Manager', '5', '110000'],
    ['Region Manager', '6', '150000'],
    ['Partner', '7', '200000'],
    ['Senior Partner', '8', '300000'],
    ['C-Level', '9', '500000'],
    ['CEO', '10', '1000000']
    
    
]

# Specify the file path
file_path = '/Users/jogbaner/Polynomial Regression/Salary.csv'

# Write the data to the CSV file
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Salary data CSV file has created successfully at {file_path}")