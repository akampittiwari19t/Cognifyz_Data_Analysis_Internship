import pandas as pd 

df =pd.read_csv("Dataset .csv")

# City with highest number of restaurants

city_count=df['City'].value_counts()
print("city with Highest number of Resturanats:")
print(city_count.head(1))

# Average rating by city

avg_rating=df.groupby('City')['Aggregate rating'].mean ()
print("\nAverage Rating by city:")
print(avg_rating)

# City with highest average rating
highest_rating_city = avg_rating.idxmax()
highest_rating = avg_rating.max()

print("\nCity with Highest Average Rating:")
print(highest_rating_city, "-", round(highest_rating, 2))