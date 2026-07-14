import numpy as np

tmp_data = [1.0, 2.3, 3.4, 4.5, 5.7, 6.9, 7.6, 9.8, 10.2, 11.1, 12.7, 13.4, 14.4, 15.6, 16.9, 17.4, 18.8, 19.0, 20.3, 21.1, 22.8, 23.7, 24.7]

np_temp = np.array(tmp_data)
print(np_temp)
print(np_temp.shape)
print(np_temp.dtype)

print(np_temp[12])

np_temp[14] = -1
print(np_temp)

print(np_temp[10:19])

np_temp = np.delete(np_temp, 14)
print(np_temp)

median_temp = np.median(np_temp)
np_temp = np.insert(np_temp, 14, median_temp)
print(np_temp)

min_val = np.min(np_temp)
min_time = np.argmin(np_temp)
print(min_val, min_time)

max_val = np.max(np_temp)
max_time = np.argmax(np_temp)
print(max_val, max_time)

std_dev = np.std(np_temp)
print(std_dev)
