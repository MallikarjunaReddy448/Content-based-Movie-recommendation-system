from fuzzywuzzy import process
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os
import ast 

# Load dataset and preprocessed data at the start (global variables for the app)
Movies_dataset = pd.read_csv("Movies_dataset")

# Loding the presaved vectorizer and matrix

with open("tfidf_final_vectorizer.pkl", 'rb') as f:
    tfidf = pickle.load(f)

with open("tfidf_final_matrix.pkl", 'rb') as f:
    tfidf_matrix = pickle.load(f)

def recommend_movies(movie_title, genre=None, top_n=20):
    # check if the movie title is already in the list of movies dataset
    if movie_title not in Movies_dataset["Movie Name"].values:
        print(f"{movie_title} is not found in our database. Trying to recommend based on fuzzy movie matching.")

        # Fuzzy matching to find the closest movie match from the database
        closest_match = process.extractOne(movie_title, Movies_dataset["Movie Name"])

        if closest_match:
            print(f"Did you mean '{closest_match[0]}'? Providing recommended movies based on this movie")
            movie_title = closest_match[0]  # Update movie title with the closest match
            user_input = f"{movie_title} {genre}" if genre else movie_title
        else:
            print("No similar movies found. Providing recommendations based on the genre")
            if not genre:
                return []  # No recommendations if neither movie nor genre is provided
            user_input = genre
    else:
        user_input = f"{movie_title} {genre}" if genre else movie_title
    
    # Vectorizing the user input
    user_vector = tfidf.transform([user_input])
    cosine_sim = cosine_similarity(user_vector, tfidf_matrix).flatten()

    if genre:
        genre_vector = tfidf.transform([genre])
        genre_cosine_sim = cosine_similarity(genre_vector, tfidf_matrix).flatten()

        # Combining cosine similarity scores
        combined_score = cosine_sim + 0.5 * genre_cosine_sim
    else:
        combined_score = cosine_sim

    # Get the top indices of movies with highest combined similarity score
    top_indices = combined_score.argsort()[-top_n:][::-1]

    # Exclude the input movie from recommendations
    if movie_title in Movies_dataset['Movie Name'].values:
        input_index = Movies_dataset[Movies_dataset['Movie Name'] == movie_title].index[0]
        combined_score[input_index] = -1  # Set the score to a very low value to exclude the input movie

    # Fetch recommended movie titles with additional details
    recommended_movies = Movies_dataset.iloc[top_indices][['Movie Name', 'Genre', 'Movie Release Year']].to_dict('records')

    for movie in recommended_movies:
    #     # movie['Genre'] = ', '.join([genre.strip() for genre in movie['Genre'].split(',')]) if movie["Genre"] else ''
    #     # movie['Genre'] = ast.literal_eval(movie['Genre'])
        movie["Genre"] = movie["Genre"].split(',') if movie["Genre"] else []

    # Format movie details for rendering in the frontend
    for movie in recommended_movies:
        movie['Movie_Name'] = movie.pop('Movie Name')
        movie['Movie_Release_Year'] = movie.pop('Movie Release Year')
        movie['Genre'] = ', '.join(movie['Genre'])
        # movie['Genre'] = movie['Genre']

    return recommended_movies
