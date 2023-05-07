import book
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import plotly.express as px


# Scrape data from source
x = book.Scraper()
x.selfHelpBooks()

# Reading the scraped data
df = pd.read_csv("books.csv")

print(df.head())

print(df.describe())

print(df.info())

print(df["year"].unique())

# Extracting the year from the string of date
df["year"] = df["year"].str.replace(r"((\d{0,2})\s(\w{0,5})\s)", "")

print(df["year"].unique())

# This shows the number of each book per year
print(df.groupby(['year']).count())

# Visualizing the year column in a table
year_count = df.groupby('year').size().reset_index(name='Count')

# Create a bar chart to visualize the distribution of years
fig, ax = plt.subplots(figsize=(10, 7))  # Set the width to 10 inches
ax.bar(year_count['year'], year_count['Count'])
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.set_title('Distribution of Years')

ax.set_xticklabels(year_count['year'], rotation=90)

plt.show()

# Removing the dollar sign from the prices and converting it to a float
df["price"] = df["price"].str.extract(r"(\d{1,3}\.\d{1,3})", expand=False)
df["price"] = df["price"].astype("Float64")
print(df["price"])

# Checking me mean prices of books
print(f'The average price of books on Amazon is: {df["price"].mean()}')

# Visualizing the most common words in the book title
text = " ".join(i for i in df.title)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords,
                      background_color="white").generate(text)
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Visualizing the Top 10 authors with the most books
counts = df['author'].value_counts()
df_count = pd.DataFrame({'author': counts.index, 'count': counts.values})
print(df_count.head(10))
fig = px.bar(df_count.head(10), x='author', y='count')
fig.show()

# Getting the name of the most expensive book
maxPrice = df['price'].max()
print(
    f'The most expensive book is: {df[df["price"] == maxPrice].title} and it costs {df[df["price"] == maxPrice].price}')
