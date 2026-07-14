import numpy as np

def clean_outlier(arr):
    q1 = np.percentile(arr, 25)
    q3 = np.percentile(arr, 75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    median = np.median(arr)
    return np.where((arr < lower) | (arr > upper), median, arr)

def clean_outlier_std(arr):
    mean = np.mean(arr)
    std = np.std(arr)
    lower = mean - 2 * std
    upper = mean + 2 * std
    median = np.median(arr)
    return np.where((arr < lower) | (arr > upper), median, arr)

def clean_invalid(arr):
    clean_arr = arr.copy()
    indices = np.where(arr == -1)[0]
    for idx in indices:
        neighbors = []
        if idx > 0 and arr[idx - 1] != -1:
            neighbors.append(arr[idx - 1])
        if idx < len(arr) - 1 and arr[idx + 1] != -1:
            neighbors.append(arr[idx + 1])
        if neighbors:
            clean_arr[idx] = np.mean(neighbors)
    return clean_arr

def fix_invalid_data(arr, axis=None):
    if axis is None:
        mask = arr == -999
        mean_val = np.mean(arr[~mask])
        return np.where(mask, mean_val, arr)
        
    def replace_func(line):
        mask = line == -999
        mean_val = np.mean(line[~mask])
        return np.where(mask, mean_val, line)

    return np.apply_along_axis(replace_func, axis, arr)