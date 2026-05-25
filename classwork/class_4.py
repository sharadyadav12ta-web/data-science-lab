import matplotlib .pyplot as plt

#x = [2, 3, 4, 6, 6]
#y = [4, 6, 8, 12, 12]
#fig, ax = plt.subplots()
#ax.plot(x, y)
#ax.set_xlabel("X values")
#ax.set_ylabel("Y values")
#ax.set_title("plot of 2x = y")
#plt.show()


#y_values = []
#x_values = []
#for x in range(-20, 20):
 #   y = 3 * x ** 2
  #  x_values.append(x)
   # y_values.append(y)

#fig, ax = plt.subplots()
#ax.plot(x_values, y_values)
#ax.set_xlabel("X values")
#ax.set_ylabel("Y values")
#ax.set_title("plot of 3x^2 = y")
#plt.show()

#y_values = []
#y2_values = []
#x_values = []
#for x in range(-20, 21):
 #   y = 3 * x ** 2 + 4 * x - 3
  #  y2 = 4 * x - 5
   # x_values.append(x)
    #y_values.append(y)
    #y2_values.append(y2)

#fig, ax = plt.subplots()
#ax.plot(x_values, y_values, label= "3x^2 + 4x - 3")
#x.plot(x_values, y2_values, label= "4x - 5")
#ax.set_xlabel("X values")
#ax.set_ylabel("Y values")
#ax.legend()
#ax.set_title("plot of 3x^2 = y")
#plt.show()


import pandas as pd
file_path_2 = r"C:\Users\vs\Downloads\2022-01-02.csv"
df_2 = pd.read_csv(file_path_2)

print(df_2.dtypes)

fig, ax = plt.subplots()
ax.scatter(df_2["Close - LTP %"], df_2["Diff %"])
plt.show()