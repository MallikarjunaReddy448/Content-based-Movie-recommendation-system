from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
import pickle
from .utils import recommend_movies
from django.core.mail import send_mail
import os
from django.conf import settings


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
        
        # # Save the suggestion to the database (optional)
        # suggestion = MovieSuggestion(user_name=user_name, user_email=user_email, movie_name=movie_name, movie_genre=movie_genre)
        # suggestion.save()

        # Send the suggestions via email
        subject = f"New Movie Suggestion from {user_name}"
        message = f"Dear Team please add the below movie information to your database \nMovie Name: {movie_name} \nGenre: {movie_genre or 'Not Provided'} \nUser Name: {user_name} and email: {user_email}"
        sender_mail = settings.EMAIL_HOST_USER
        reciepient_list = ['mallikarjunreddy448@gmail.com']
        # send_mail(subject, message, sender_mail, reciepient_list, fail_silently=True)

        try:
            send_mail(subject, message, sender_mail, reciepient_list, fail_silently=False)
            response_message = f"Thank you for your suggestion '{movie_name}'! We’ll look into adding it. \n Please try another movie you have seen recently and get some recommendations."
        except Exception as e:
            response_message = f"Error sending email: {str(e)}"

        return render (request, 'feedback_response.html', {'response_message': response_message})

    return render(request, 'contact_feedback.html')
