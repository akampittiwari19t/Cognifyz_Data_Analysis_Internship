import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset .csv")

# Count restaurants in each price range
price_range_count = df['Price range'].value_counts().sort_index()

print("Price Range Distribution:")
print(price_range_count)

# Percentage
percentage = (price_range_count / len(df)) * 100

print("\nPercentage of Restaurants:")
print(percentage.round(2))

# Bar Chart
plt.bar(price_range_count.index, price_range_count.values)
plt.title("Price Range Distribution")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.show()