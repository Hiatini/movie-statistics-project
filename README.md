# 📌 Movie Statistic Project : Using Netflix 

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


### Genre

The next question concerns the film genre. What is the most popular genre and what is the proportion of this genre? 

![Capture d’écran 2024-01-04 à 22 05 19](https://github.com/Hiatini/movie-statistics-project/assets/101217055/ede57685-7f4a-482a-b1dd-f4ed6cdd6e94)

The three best-known genres are Documentary, Comedy and Drama. Documentaries have a percentage of 30%, in other words, 30% of the films present are documentaries. 

### Runtime 

Let's make a runtime histogram to understand how long most movies are.

![Capture d’écran 2024-01-04 à 23 06 42](https://github.com/Hiatini/movie-statistics-project/assets/101217055/222f2a88-849d-44d0-ab4b-c7ea80ff455c)

The mean runtime is 100 minutes with a standard deviation of 27.76 minutes. This means that most films are around 100 minutes long, but individual films might be as short as around 72.24 minutes or as long as around 127.76 minutes. The standard deviation helps you understand the range of variation in film runtimes.

