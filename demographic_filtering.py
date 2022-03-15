# Import all modules
import pandas as pd
import numpy as np

# Read the file
df = pd.read_csv('final.csv')

# Weighted_rating formula values 
C = df['vote_average'].mean()   # Vote average
m = df['vote_count'].quantile(0.9)  # Vote count
q_movies = df.copy().loc[df['vote_count'] >= m]

# Calculation
def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

q_movies = q_movies.sort_values('score', ascending=False)

# Get the top 20 movies stored in the output var
output = q_movies[['title', 'poster_link', 'release_date', 'runtime', 'vote_average', 'overview']].head(20).values.tolist()