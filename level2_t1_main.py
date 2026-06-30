import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv("Dataset .csv")

# rating distribution

rating_count=df['Aggregate rating'].value_counts().sort_index()
print("rating Distribution:")
print(rating_count)

# Most common rating
most_common_rating = df['Aggregate rating'].mode()[0]
print("\nMost Common Rating:", most_common_rating)

# Average votes
avg_votes = df['Votes'].mean()
print("Average Votes:", round(avg_votes, 2))

# Graph
plt.hist(df['Aggregate rating'], bins=10)
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.show()