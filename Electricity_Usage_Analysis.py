'''import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr)

reshaped = arr.reshape(3,4)
print(reshaped)

array = ([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
flattened = reshaped.flatten()
print(flattened)

flattened = reshaped.flatten()
flattened[0] = 99
print(flattened)
print(reshaped)

reveled = reshaped.ravel()
reveled[1] = 88
print(reveled)

print(reshaped)

arr1 = np.array([1,2,3])
print(arr1)
arr2 = np.array([2,3,4])
print(arr2)

print(arr1+arr2)
print(arr1+4)

arr1 = np.array([1,2,3])
print(arr1)
arr2 = np.array([[2],[4],[6]])
print(arr2)

print(arr1+arr2)'''

import numpy as np  
import pandas as pd
np.random.seed(42)
apartments = [f"Apt_{i}" for i in range(1, 21)]
dates = pd.date_range(start="2025-07-15", periods=30, freq="D")
data = {"date":np.tile(dates , len(apartments)),
        "Apartment":np.repeat(apartments,len(dates)),
        "Electricity_usage":np.random.normal(loc=20,scale=5,size=len(dates)*len(apartments))}
df = pd.DataFrame(data)
df["Electricity_usage"]= df["Electricity_usage"].round(2)
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)
usage_by_apartment = df.groupby("Apartment")["Electricity_usage"].sum().sort_values(ascending=False)   
print(usage_by_apartment)
daily_avg = df.groupby("date")["Electricity_usage"].mean()
print(daily_avg.head())


import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(12, 6))
sns.barplot(x=usage_by_apartment.index, y=usage_by_apartment.values)
plt.xticks(rotation=90)
plt.title("TOTAL USAGE PER APARTMENT")
plt.xlabel("Apartment")
plt.ylabel("Total KWH")
plt.tight_layout()
plt.show()     


plt.figure(figsize=(12, 6))
sns.lineplot(x=daily_avg.index, y=daily_avg.values)
plt.title("DAILY AVERAGE ELECTRICITY USAGE")
plt.xlabel("Date")
plt.ylabel("Average KWH")
plt.tight_layout()
plt.show()


thrshold = df["Electricity_usage"].mean() + 2 * df["Electricity_usage"].std()
df["High_usage"] = df["Electricity_usage"] > thrshold
print(df[df["High_usage"] == True].head())