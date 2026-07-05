# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python, Flask, and Scikit-learn that recommends similar movies based on genres, cast, keywords, directors, and movie overviews. The application uses the TMDB 5000 Movies Dataset and is deployed on Railway for public access.

---

## 📌 Features

* Content-based movie recommendations
* Uses the TMDB 5000 Movies Dataset
* Cosine similarity for finding similar movies
* Interactive Flask web interface
* Clean and responsive UI
* Ready for deployment on Railway

---

## 🛠️ Tech Stack

| Technology   | Purpose                                |
| ------------ | -------------------------------------- |
| Python       | Backend Development                    |
| Pandas       | Data Processing                        |
| NumPy        | Numerical Computations                 |
| Scikit-learn | Vectorization & Similarity Calculation |
| Flask        | Web Framework                          |
| HTML/CSS     | Frontend                               |
| Gunicorn     | Production Server                      |
| Railway      | Cloud Deployment                       |

---

## 📂 Project Structure

```text
movie-recommendation-system/
│
├── app.py
├── create_model.py
├── requirements.txt
├── Procfile
├── README.md
├── movies.pkl
├── similarity.pkl
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## 📊 Dataset

This project uses the **TMDB 5000 Movies Dataset**, which contains information about thousands of movies, including:

* Genres
* Cast
* Crew
* Keywords
* Overviews
* Ratings
* Release Information

Download the dataset from:

https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Place the following files inside the `data/` folder:

```text
tmdb_5000_movies.csv
tmdb_5000_credits.csv
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git

cd movie-recommendation-system
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Generate the Recommendation Model

Run the preprocessing script to create the model files:

```bash
python create_model.py
```

This generates:

```text
movies.pkl
similarity.pkl
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🧠 Recommendation Algorithm

The system follows a content-based filtering approach:

1. Merge movie and credits datasets.
2. Extract important features:

   * Genres
   * Keywords
   * Cast
   * Directors
   * Movie Overview
3. Combine these features into tags.
4. Convert text into vectors using CountVectorizer.
5. Compute cosine similarity between movies.
6. Recommend the top 5 most similar movies.

---

## ☁️ Deployment on Railway 
Live link:-
https://web-production-a58820.up.railway.app/

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

---

## 📸 Application Preview

```text
🎬 Movie Recommendation System

[Select a Movie ▼]

[Recommend]

Recommended Movies:
• Interstellar
• The Prestige
• The Dark Knight
• Avatar
• Titanic
```

---

## 🔮 Future Improvements

* Movie poster integration using the TMDB API
* Search bar with autocomplete
* User authentication
* Collaborative filtering recommendations
* Hybrid recommendation engine
* Docker support
* CI/CD pipeline using GitHub Actions

---

## 👨‍💻 Author

**Anshul Deep Bajpai**

B.Tech CSE (AI & ML) | AI & Data Science Enthusiast


---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
