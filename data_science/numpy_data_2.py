import csv
import numpy as np

np.random.seed(101)
data_size = 100

first_names = ["Ram", "Shyam", "Sita", "Gita", "Hari", "Ravi", "Aman", "Pooja"]
last_names = ["Sharma", "Verma", "Singh", "Jha", "Khan", "Kumar", "Joshi", "Das"]

roll_no = np.arange(1, data_size + 1)
first_name = np.random.choice(first_names, size=data_size)
last_name = np.random.choice(last_names, size=data_size)
age = np.random.randint(18, 26, size=data_size)
height = np.random.normal(160.0, 20.0, size=data_size)
rating = np.random.uniform(1.0, 5.0, size=data_size)

rows = zip(roll_no, first_name, last_name, age, height, rating)

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["RollNo", "FirstName", "LastName", "Age", "Height", "Rating"])
    writer.writerows(rows)