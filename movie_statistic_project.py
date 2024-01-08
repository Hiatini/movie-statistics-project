# # 📌 Movie Statistics Project : Using Netflix

### Introduction
# Hello everyone! Forwarding my career in data, I want to strengthen my knowledge by using Netflix Movies and Documentaries. By doing it, I hope you will enjoy the process.


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import squarify 
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

df = pd.read_csv("/kaggle/input/netflix-original-films-imdb-scores/NetflixOriginals.csv", encoding='ISO-8859-1')
df.info()
df = df.rename(columns={"Premiere": "Year", "IMDB Score": "Score"})
df2 = pd.DataFrame(df)
df2

#### Language
# 
# First, I decided to start with the language variable. We'll see about languages and their relationship with each movie. Let's see how many movies we have in each language.

number_of_movies_per_language = df['Language'].value_counts().reset_index()
number_of_movies_per_language.columns = ['Language', 'Number of movies']

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(number_of_movies_per_language['Number of movies'], labels=number_of_movies_per_language['Language'], autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Ensure the pie chart is circular
plt.title('Films by Language')

# Display the pie chart
plt.show()

# The following table shows the number of films in each language. With this in mind, I'll start by understanding what the different languages of the films are. From the graphs, we can see that we have 4 languages: English, Spanish, Hindi, and French. We'll also be interested in seeing which films are translated into just one language and which have several languages available for the film.

correspondance_langues = {
    'English': 'English',
    'Spanish': 'Spanish',
    'Hindi': 'Hindi',
    'French': 'French',
}

# Replace specific values using the dictionary
df['Language'] = df['Language'].replace(correspondance_langues)

# Replace remaining values with 'Other Single'
df['Language'] = df['Language'].fillna('Other Single')

# Alternatively, we can use the following one-liner
# df['Language'] = df['Language'].replace(correspondance_langues).fillna('Other Single')

# List of primordial languages
primary_languages = {'English', 'Spanish', 'Hindi', 'French'}

# Replace multiple languages and create a new 'Category' column
df['Category'] = np.where(df['Language'].str.contains('/'), 'Multiples', 'Single')

# Replace specific languages and create a new 'Language' column
df['Language'] = df.apply(lambda row: 'Other Single' if row['Category'] == 'Single' and row['Language'] not in primary_languages else row['Language'], axis=1)

# Create a new column 'Language_Category' using np.where
df['Language_Category'] = np.where(df['Category'] == 'Multiples', 'Multiples', df['Language'])

# Display updated dataframe
df[['Title', 'Language_Category']]

language_category_counts = df['Language_Category'].value_counts()

# Show countdown
print(language_category_counts)

# #### Faced with our results, we're going to ask ourselves three questions: 

# 1. Clearly, there are many films whose main language is English. Of the 584 films, what is the proportion whose main language is English? 

# To determine the proportion of films with English as their main language among the 584 films, we can use the equation 401/584, resulting in approximately 0.69, indicating that around 69% of the movies are in English.

# 2. What is the ratio of English-language films to films in a single language other than English? 

# With a ratio of 401/160, we find that there are almost 5 English films for every 2 films in a language other than English. In a hypothetical set of 50 films, this ratio implies having approximately 14 (=(2/7)/50) films in a language other than English and about 36(=(5/7)/50) films in English.

# 3. What is the proportion of films with multiple main languages?

# Building on the insights from the first question, let's consider the films labeled as 'multiples.' The division of 23 by 584 results in approximately 0.039, indicating that about 3% of the movies feature languages other than English, Spanish, French, Hindi, etc.

# Just for Fun: About 3% of the films have multiple primary languages. Let's find out which genres tend to have this interesting feature. First, let's see our code :

# Filter lines where the language category is "Multiples".
multiples_df = df[df['Language_Category'] == 'Multiples']

# Perform a frequency analysis on the film genre in these rows
genre_counts = multiples_df['Genre'].value_counts()

# Display the result
print("Frequency of film genres associated with 'Multiples':")
print(genre_counts)

# The majority of films containing multiple languages are documentaries. It can be hypothesized that since this is a work of research, analysis and entertainment, the aim is to share documentaries with as many people as possible.

#### Genre

# Filter rows where gender appears less than 20 times
genre_counts_filtered = df['Genre'].value_counts()
genre_counts_filtered = genre_counts_filtered[genre_counts_filtered >= 20]

# Calculate percentages
total_films = len(df)
genre_pourcentages = genre_counts_filtered / total_films * 100

# Draw a bar chart to visualize the distribution of genres associated with 'Multiples'.
plt.figure(figsize=(12, 6))
sns.barplot(x=genre_pourcentages.index, y=genre_pourcentages.values, palette='viridis')
plt.title('Distribution of film genres')
plt.xlabel('Film genre')
plt.ylabel('Percentage of total films')
plt.xticks(rotation=45, ha='right')

# Add annotations to display percentages on each bar
for i, percentage in enumerate(genre_pourcentages) :
    plt.text(i, percentage + 0.25, f'{percentage :.2f}%', ha='center', va='bottom')

plt.show()

# The three best-known genres are Documentary, Comedy and Drama. Documentaries have a percentage of 30%, in other words, 30% of the films present are documentaries.

### Runtime 

# Let's make a runtime histogram to understand how long most movies are.

# Plot an histogram to visualize the distribution of runtime
plt.figure(figsize=(12, 6))
sns.histplot(df['Runtime'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Film Runtimes')
plt.xlabel('Runtime (minutes)')
plt.ylabel('Frequency')
plt.show()

# Filter rows where runtime appears less than 20 times
runtime_counts_filtered = df['Runtime'].value_counts()

# Calculate the mean runtime
average_runtime = df['Runtime'].mean()

# Print the average runtime
print(f"Average Runtime: {average_runtime:.2f} minutes")

# Calculate the standard deviation of the runtime
std_dev_runtime = df['Runtime'].std()

# Print the standard deviation of the runtime
print(f"Standard Deviation of Runtime: {std_dev_runtime:.2f} minutes")

# The mean runtime is 93.58 minutes with a standard deviation of 27.76 minutes. This means that most films are around 100 minutes long, but individual films might be as short as around 72.24 minutes or as long as around 127.76 minutes. These measurements are not wrong, but they don’t help us do a good job of summarizing what we’re seeing in the distribution.

# Based on the distribution plot, what is your guess for the median and IQR of runtimes? Find out if your guess was close!

# Calculate the median and interquartile range (IQR) of runtimes
median_runtime = df['Runtime'].median()
q1_runtime = df['Runtime'].quantile(0.25)
q3_runtime = df['Runtime'].quantile(0.75)
iqr_runtime = q3_runtime - q1_runtime

# Print the results
print(f"Actual Median Runtime: {median_runtime:.2f} minutes")
print(f"Actual IQR of Runtime: {iqr_runtime:.2f} minutes")

# On the contrary, the median characterizes a runtime that is higher and represents the most typical scenario. The low Interquartile Range (IQR) suggests that half of the values are relatively close to the central value. These descriptions align well with the substantial concentration of values around 100, as observed in the distribution plot.

# Given that the mean is lower than the median, it appears that the left-skew has a more pronounced impact on the mean than the potential outlier on the higher end.

### IMDb Score

# Are most films rated around the same score? Are there some extremely low or high scores?

# Plot an histogram to visualize the distribution of IMDb Score
plt.figure(figsize=(12, 6))
sns.histplot(df['Score'], bins=30, kde=True, color='blue')
plt.title('Distribution of Film Imbd Score')
plt.xlabel('IMDb Score')
plt.ylabel('Frequency')
plt.show()

# Filter rows where runtime appears less than 20 times
runtime_counts_filtered = df['Score'].value_counts()

# Calculate the mean IMDb Score
average_runtime = df['Score'].mean()

# Print the average IMDb Score
print(f"Average IMDb Score: {average_runtime:.2f}.")

# Calculate the standard deviation of the IMDb Score
std_dev_runtime = df['Score'].std()

# Print the standard deviation of the IMDb Score
print(f"Standard Deviation of IMDb Score: {std_dev_runtime:.2f}.")

# The mean IMDb Score is 6.27 with a standard deviation of 0.98. This means that most IMDb Score films are around 6.27, but individual IMDb Score films might be as short as around 7.25 or as long as around 5.29. The standard deviation helps you understand the range of variation in IMDb Score films.If a distribution exhibits a relatively symmetrical pattern without significant outliers, the mean serves as a reliable indicator of a "typical" value, while the standard deviation informs us whether most scores cluster around this typical value or if there is a broad range of scores.

# Now, let's find out which films got the highest and lowest IMDb scores!

# Table of the 5 highest IMDb scores
top_scores = df.nlargest(5, 'Score')[['Title', 'Score']]

# Table of the 5 lowest IMDb scores
bottom_scores = df.nsmallest(5, 'Score')[['Title', 'Score']]

# Show tables
print("Top 5 IMDb Scores:")
print(top_scores)

print("\nBottom 5 IMDb Scores:")
print(bottom_scores)

# ## Relationships

# ### IMDb Score by Genre

# We want to know if any genres have particularly high IMDb scores, so you look at a table of means and standard deviations of IMDb scores for each genre.

# List of genres you're interested in
selected_genres = ["Action/Science-fiction", "Animation", "Comedy", "Documentary", "Drama", "Horror/Thriller", "Other", "Romance/Romantic Comedy"]

# Filter the DataFrame to include only the selected genres
selected_genre_df = df[df['Genre'].isin(selected_genres)]

# Group the data by genre and calculate the mean IMDb score for each genre
genre_imdb_mean = selected_genre_df.groupby('Genre')['Score'].mean().sort_values(ascending=False)

# Group the data by genre and calculate the standard deviation IMDb score for each genre
genre_imdb_std = selected_genre_df.groupby('Genre')['Score'].std().sort_values(ascending=False)


# Create a DataFrame to display the results
result_df = pd.DataFrame({
    'Genre': genre_imdb_mean.index,
    'Average IMDb Score': genre_imdb_mean.values,
    'Standard Deviation IMDb Score': genre_imdb_std.values
})

# Print the DataFrame
print(result_df)

# ### Runtime by Language
# You are exploring whether there are variations in the duration of movies based on different languages.

# Extracting the number of languages from the "Language" column
df['Num_Languages'] = df['Language'].apply(lambda x: len(x.split('/')))

# Create a new column "Language_Category" based on the number of languages
df['Language_Category'] = np.where(df['Num_Languages'] > 1, 'Multiples', df['Language'])

# Calculate mean and standard deviation for each language category
mean_duration_by_category = df.groupby('Language_Category')['Runtime'].mean().reset_index()
std_dev_duration_by_category = df.groupby('Language_Category')['Runtime'].std().reset_index()

# Merge the dataframes to create the final table
result_table = pd.merge(mean_duration_by_category, std_dev_duration_by_category, on='Language_Category', suffixes=('_mean', '_std'))

# Rename the columns for clarity
result_table = result_table.rename(columns={'Runtime_mean': 'Mean Duration', 'Runtime_std': 'Standard Deviation'})

# Print the result table
print(result_table[['Language_Category', 'Mean Duration', 'Standard Deviation']])

# In the "English" category with an average duration of approximately 91.82 minutes and a standard deviation of around 28.51 minutes, this implies that the duration of English films can typically vary by about 28.51 minutes around the mean.

# In simpler terms, if you watch an English film, you can expect the duration to be close to 91.82 minutes. However, due to the typical variation of 28.51 minutes, some films may be shorter (e.g., around 63.31 minutes), and others may be longer (e.g., around 120.33 minutes). The standard deviation quantifies this spread, providing an indication of the variability in film durations within the language category.

# Therefore, a higher standard deviation suggests a greater variability of values around the mean, while a lower standard deviation implies less dispersion.

# Scatter plot of Runtime vs IMDb Score
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Runtime', y='Score', data=df, color='green', alpha=0.7)
plt.title('Runtime vs. IMDb Score')
plt.xlabel('Runtime (minutes)')
plt.ylabel('IMDb Score')
plt.show()

# The strength of a linear relationship between variables is reflected in the appearance of the scatter plot. A strong positive relationship is evident when points form a pattern from the bottom-left to the top-right of the plot, while a strong negative relationship is characterized by points running from the bottom-right to the top-left. In this case, the scatter plot does not display a clear linear relationship between the two variables. Instead, it predominantly exhibits a cluster of points without a distinct line shape.

# There is no discernible trend indicating that lower runtimes are consistently associated with either low or high IMDb scores, and the same holds for higher runtimes. The majority of films in the dataset have runtimes ranging from 50 to 150 minutes. Across this range, IMDb scores vary between approximately 6.0 and 8.0, with no specific pattern or correlation observed.

# Calculate the correlation coefficient between IMDb Scores and Runtimes
correlation_coefficient = df['Score'].corr(df['Runtime'])

# Print the result
print(f"Correlation Coefficient between IMDb Scores and Runtimes: {correlation_coefficient:.2f}")

# The true correlation coefficient is -0.04. The sign indicates a negative relationship, but the value is so close to zero that we should conclude there's really no linear relationship between the variables.