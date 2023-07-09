import random
import csv

# Generate a list of 1000 randomized values from 0 to 100
values = [str(random.randint(0, 100)) for _ in range(1000)]

# Specify the filename for the CSV file
filename = 'random_values.csv'

# Write the values to the CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['value'])  # Write the header row
    writer.writerows([[value] for value in values])  # Write the randomized values

print(f"CSV file '{filename}' has been created with 1000 randomized entries.")
