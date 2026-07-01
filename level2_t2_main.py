import pandas as pd

df = pd.read_csv("Dataset .csv")

# Top cuisine combinations
top_combinations = df['Cuisines'].value_counts().head(10)

print("Top 10 Cuisine Combinations:")
print(top_combinations)

# Average rating by cuisine combination
avg_rating = df.groupby('Cuisines')['Aggregate rating'].mean()

print("\nTop Cuisine Combinations with Ratings:")
print(avg_rating.sort_values(ascending=False).head(10))