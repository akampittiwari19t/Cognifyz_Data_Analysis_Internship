import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset .csv")

print("Latitude Summary:")
print(df['Latitude'].describe())

print("\nLongitude Summary:")
print(df['Longitude'].describe())

# Scatter Plot
plt.figure(figsize=(8,6))
plt.scatter(df['Longitude'], df['Latitude'], alpha=0.5)

plt.title("Restaurant Locations")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.show()