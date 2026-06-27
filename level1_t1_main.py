import pandas as pd

df =pd.read_csv("Dataset .csv")
print(df.head())

print(df['Cuisines'].head())

top_cuisines=df['Cuisines'].str.split(',').explode().value_counts().head(3)
print(top_cuisines)

percentage = (top_cuisines / len(df)) * 100
print(percentage.round(2))