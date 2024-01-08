![image](https://github.com/Hiatini/movie-statistics-project/assets/101217055/bbf2a6b1-6451-41d7-a737-6a9241fc0728)![image](https://github.com/Hiatini/movie-statistics-project/assets/101217055/fe2cd7bb-f045-4f96-8662-15b33bc9c6de)# 📌 Movie Statistic Project : Using Netflix 

As part of this project, I'm tasked with researching the content produced by streaming services, particularly Netflix, over the past few years. I'm gathering information for a report on the types of films being produced, as well as trends worth exploring further. 

## Dataset

I decided to start my research by exploring some data about films and documentaries produced by Netflix. I will use a dataset on Kaggle : https://www.kaggle.com/datasets/luiscorter/netflix-original-films-imdb-scores/data. My dataset included 503 films with the following variables : 

* title: title of the film
* genre: genre of the film
* language: primary language of the film
* year: year the film premiered
* runtime: length of the film in minutes
* score: film rating of 1 to 10 (worst to best) from the website IMDb

## Individual Variables
### Language

First, I decided to start with the language variable. The following table shows the number of films in each language. With this in mind, I'll start by understanding what the different languages of the films are. From the graphs, we can see that we have 4 languages: English, Spanish, Hindi and French. We'll also be interested to see which films are translated into just one language, and which have several languages available for the film.

![Capture d’écran 2023-11-08 à 00 23 30](https://github.com/Hiatini/movie-statistics-project/assets/101217055/c8481b13-d901-418c-ae37-f1ce5cf34163)

![Capture d’écran 2024-01-04 à 15 36 23](https://github.com/Hiatini/movie-statistics-project/assets/101217055/6f7b07f9-971f-40a6-a1d7-0c37b35201b5)

#### Faced with our results, we're going to ask ourselves three questions: 

1. Clearly, there are many films whose main language is English. Of the 584 films, what is the proportion whose main language is English? 

To determine the proportion of films with English as their main language among the 584 films, we can use the equation 401/584, resulting in approximately 0.69, indicating that around 69% of the movies are in English.

2. What is the ratio of English-language films to films in a single language other than English? 

With a ratio of 401/160, we find that there are almost 5 English films for every 2 films in a language other than English. In a hypothetical set of 50 films, this ratio implies having approximately 14 (=(2/7)/50) films in a language other than English and about 36(=(5/7)/50) films in English.

3. What is the proportion of films with multiple main languages?

Building on the insights from the first question, let's consider the films labeled as 'multiples.' The division of 23 by 584 results in approximately 0.039, indicating that about 3% of the movies feature languages other than English, Spanish, French, Hindi, etc.

4. Just for Fun: About 2,5% of the films have multiple primary languages. Let's find out which genres tend to have this interesting feature. First, let's see our code :

![Capture d’écran 2024-01-04 à 21 40 30](https://github.com/Hiatini/movie-statistics-project/assets/101217055/777d779b-91af-4300-bbff-bcea6bc032df)

The majority of films containing multiple languages are documentaries. It can be hypothesized that since this is a work of research, analysis and entertainment, the aim is to share documentaries with as many people as possible. 

### IMDb Score

Are most films rated around the same score? Are there some extremely low or high scores?

![Capture d’écran 2024-01-06 à 00 06 42](https://github.com/Hiatini/movie-statistics-project/assets/101217055/2834bdf0-7d13-4ce2-a1a6-fc9971251b3f)

The mean IMDb Score is 6.27 with a standard deviation of 0.98. This means that most IMDb Score films are around 6.27, but individual IMDb Score films might be as short as around 7.25 or as long as around 5.29. The standard deviation helps you understand the range of variation in IMDb Score films. If a distribution exhibits a relatively symmetrical pattern without significant outliers, the mean serves as a reliable indicator of a "typical" value, while the standard deviation informs us whether most scores cluster around this typical value or if there is a broad range of scores.

Now, let's find out which films got the highest and lowest IMDb scores!

![Capture d’écran 2024-01-06 à 00 39 19](https://github.com/Hiatini/movie-statistics-project/assets/101217055/1f618e87-605b-4fce-b187-7b6b0aa40f21)

![Capture d’écran 2024-01-06 à 00 39 36](https://github.com/Hiatini/movie-statistics-project/assets/101217055/2aff6452-8ce4-49c6-bb57-f2fcb50746c4)

### Genre

The next question concerns the film genre. What is the most popular genre and what is the proportion of this genre? 

![Capture d’écran 2024-01-04 à 22 05 19](https://github.com/Hiatini/movie-statistics-project/assets/101217055/ede57685-7f4a-482a-b1dd-f4ed6cdd6e94)

The three best-known genres are Documentary, Comedy and Drama. Documentaries have a percentage of 30%, in other words, 30% of the films present are documentaries. 

### Runtime 

Let's make a runtime histogram to understand how long most movies are.

![Capture d’écran 2024-01-04 à 23 06 42](https://github.com/Hiatini/movie-statistics-project/assets/101217055/222f2a88-849d-44d0-ab4b-c7ea80ff455c)

The mean runtime is 100 minutes with a standard deviation of 27.76 minutes. This means that most films are around 100 minutes long, but individual films might be as short as around 72.24 minutes or as long as around 127.76 minutes. These measurements are not wrong, but they don’t help us do a good job of summarizing what we’re seeing in the distribution.

![Capture d’écran 2024-01-06 à 00 48 29](https://github.com/Hiatini/movie-statistics-project/assets/101217055/bc13efcb-12b5-4761-8ad5-b805e46b0506)

On the contrary, the median characterizes a runtime that is higher and represents the most typical scenario. The low Interquartile Range (IQR) suggests that half of the values are relatively close to the central value. These descriptions align well with the substantial concentration of values around 100, as observed in the distribution plot.
Given that the mean is lower than the median, it appears that the left-skew has a more pronounced impact on the mean than the potential outlier on the higher end.

## Relationships

### IMDb Score by Genre

We want to know if any genres have particularly high IMDb scores, so you look at a table of means and standard deviations of IMDb scores for each genre. 

![Uploading Capture d’écran 2024-01-06 à 23.35.36.png…]()

### Runtime by Language

You are exploring whether there are variations in the duration of movies based on different languages.

![Capture d’écran 2024-01-08 à 23 00 05](https://github.com/Hiatini/movie-statistics-project/assets/101217055/79628227-8f78-457b-a6d6-861672b0c32b)

In the "English" category with an average duration of approximately 91.82 minutes and a standard deviation of around 28.51 minutes, this implies that the duration of English films can typically vary by about 28.51 minutes around the mean.

In simpler terms, if you watch an English film, you can expect the duration to be close to 91.82 minutes. However, due to the typical variation of 28.51 minutes, some films may be shorter (e.g., around 63.31 minutes), and others may be longer (e.g., around 120.33 minutes). The standard deviation quantifies this spread, providing an indication of the variability in film durations within the language category.

Therefore, a higher standard deviation suggests a greater variability of values around the mean, while a lower standard deviation implies less dispersion.

The strength of a linear relationship between variables is reflected in the appearance of the scatter plot. A strong positive relationship is evident when points form a pattern from the bottom-left to the top-right of the plot, while a strong negative relationship is characterized by points running from the bottom-right to the top-left. Example : 

![image](https://www.investopedia.com/thmb/2b8kkUpoknl2tKdZfbsCzI-2X54=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/TC_3126228-how-to-calculate-the-correlation-coefficient-5aabeb313de423003610ee40.png)


In this case, the scatter plot does not display a clear linear relationship between the two variables. Instead, it predominantly exhibits a cluster of points without a distinct line shape.

![Capture d’écran 2024-01-08 à 23 00 43](https://github.com/Hiatini/movie-statistics-project/assets/101217055/3b6791ae-827b-4a70-a61e-276dddaa4f61)

There is no discernible trend indicating that lower runtimes are consistently associated with either low or high IMDb scores, and the same holds for higher runtimes. The majority of films in the dataset have runtimes ranging from 50 to 150 minutes. Across this range, IMDb scores vary between approximately 6.0 and 8.0, with no specific pattern or correlation observed.

![Capture d’écran 2024-01-08 à 23 02 51](https://github.com/Hiatini/movie-statistics-project/assets/101217055/8af10a2e-9fee-4fa0-a8cc-9fc8f8325cef)

The true correlation coefficient is -0.04. The sign indicates a negative relationship, but the value is so close to zero that we should conclude there's really no linear relationship between the variables.

