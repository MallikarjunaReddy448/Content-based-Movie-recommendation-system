"# Content-based-Movie Recommendation System 🎥" 

## Overview
This project is a **Movie Recommendation Web Application** that provides movie suggestions based on user input, such as movie name and genre. The system uses a content-based filtering approach with cosine similarity for generating recommendations. 

The app is deployed and accessible at: [Movie Recommendation App](https://mallikarjunareddy.pythonanywhere.com)

---

## Features
- **Scraped Data Sources:**
  - **Hollywood:** Collected year-wise popular movie data (1990-2024) from [Letterbox](https://letterboxd.com/) using `BeautifulSoup` and `Selenium`.
  - **Indian Movies:** Scraped top movies across multiple Indian film industries (e.g., Tollywood, Bollywood, Kollywood, Mollywood, Sandalwood) from IMDb for the years 1990-2024.
  - Combined all data like movie title, cast, genre, director, overview/description of the film into a single comprehensive dataset.
  
- **Recommendation System:**
  - Uses **TF-IDF vectorization** and **cosine similarity** to recommend movies based on:
    - Movie Title
    - Genre

- **Web Application:**
  - Built using **Django** framework.
  - Deployed successfully on **PythonAnywhere**.

---

## Tech Stack
### **Languages and Libraries:**
- **Python:** Core language for data scraping and recommendation logic.
- **Libraries:** Pandas, Scikit-learn, BeautifulSoup, Selenium, FuzzyWuzzy

### **Web Framework:**
- **Django:** Backend development and web application.

### **Deployment:**
- Hosted on [PythonAnywhere](https://mallikarjunareddy.pythonanywhere.com).

---

## Data Sources
- **Hollywood Movies:**
  - Scraped from [Letterbox](https://letterboxd.com/).
  - Covers popular movies from 1990 to 2024.

- **Indian Movies (Industry-wise):**
  - Scraped from IMDb.
  - Includes films from:
    - Tollywood (Telugu)
    - Bollywood (Hindi)
    - Kollywood (Tamil)
    - Mollywood (Malayalam)
    - Sandalwood (Kannada)
  - Data spans the years 1990 to 2024.

---

## How It Works
1. **Input:** 
   - Enter a **movie name** and/or **genre**.
2. **Recommendation:** 
   - The system uses cosine similarity to find and suggest the most relevant movies.
3. **Output:** 
   - Displays a list of recommended movies along with their genres and release years.

---

## How to Run the Application Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-app.git
