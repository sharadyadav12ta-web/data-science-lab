import numpy as np

info = [["Rabindra", "Instructor"], ["Ram", "Student"], ["Shyam", "Student"]]

arr = np.array(info)
print(arr)
print(arr.shape)
print(arr.dtype)

arr = np.insert(arr, -1, ["Sita", "Student"], axis=0)
print(arr)

age_col = np.array([["30"], ["25"], ["28"], ["22"]])
arr = np.insert(arr, arr.shape[1], age_col, axis=1)
print(arr)

arr = np.delete(arr, 1, axis=0)
print(arr)

arr = np.delete(arr, 2, axis=1)
print(arr)

city_col = np.array([["Kathmandu"], ["Mumbai"], ["Newyork"]])
arr = np.hstack([arr, city_col])
print(arr)

students = arr[arr[:, 1] == "Student"]
print(students[:, 0])

rabindra_row = arr[arr[:, 0] == "Rabindra"]
print(rabindra_row[0, 1])

shyam_row = arr[arr[:, 0] == "Shyam"]
print(shyam_row[0])