import pandas as pd

df = pd.read_csv("Dataset .csv")

# Top restaurant chains
chains = df['Restaurant Name'].value_counts()

print("Top Restaurant Chains:")
print(chains.head(10))

# Average ratings of top chains
top_chains = chains.head(10).index

avg_rating = df[df['Restaurant Name'].isin(top_chains)] \
    .groupby('Restaurant Name')['Aggregate rating'].mean()

print("\nAverage Ratings of Top Chains:")
print(avg_rating.sort_values(ascending=False))
