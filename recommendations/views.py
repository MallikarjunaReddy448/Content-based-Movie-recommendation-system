from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
import pickle
from .utils import recommend_movies


# Load dataset and preprocessed data at the start (global variables for the app)
Movies_dataset = pd.read_csv(r"Movies_dataset")

# Loding the presaved vectorizer and matrix

with open("tfidf_final_vectorizer.pkl", 'rb') as f:
    tfidf = pickle.load(f)

with open("tfidf_final_matrix.pkl", 'rb') as f:
    tfidf_matrix = pickle.load(f)


def home(request):
    return render(request,'home.html')


def recommend_movies_view(request):
    if request.method == 'POST':
        movie_title = str(request.POST.get('Movie Name','')).strip()
        genre = str(request.POST.get('Genre',' ')).strip() if request.POST.get('Genre') else None

        recommendations = recommend_movies(movie_title,genre)
        
        return render(request, 'recommendations.html', {"movie_title": movie_title,"recommendations": recommendations})
    
    return redirect('home')

def contact_feedback(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        movie_name = request.POST.get('movie_name')
        movie_genre = request.POST.get('movie_genre', None)
        
        # Save the suggestion to the database (optional)
        suggestion = MovieSuggestion(user_name=user_name, user_email=user_email, movie_name=movie_name, movie_genre=movie_genre)
        suggestion.save()
        
        return HttpResponse("Thank you for your suggestion! We’ll look into adding it.")

    return render(request, 'contact_feedback.html')
