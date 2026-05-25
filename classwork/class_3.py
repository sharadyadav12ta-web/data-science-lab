import pandas as pd
#file_path = r"C:\Users\vs\Downloads\2022-01-03.csv"
#df = pd.read_csv(file_path)
#print(df.head())   # 5 rows from top
#print(df.tail())   # 5 rows from bottom
#print(df.sample(5)) #  5 random rows


file_path_2 = r"C:\Users\vs\Downloads\2022-01-02.csv"
df_2 = pd.read_csv(file_path_2)
#print(df_2.sample())

#filter_condition = df_2["Conf."] > 61.95
#filtered_data = df_2[filter_condition]
#print(filtered_data)

#filter_condition = (df_2["Conf."] > 55) & (df_2["Conf."] < 60)
#filtered_data = df_2[filter_condition]
#print(filtered_data)

filter_condition = df_2["Symbol"] == "ABDL"
filtered_data = df_2[filter_condition]
print(filtered_data)