import pandas as pd
import ast
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

# Merge datasets
movies = movies.merge(credits, on="title")

# Select required columns
movies = movies[
    [
        "movie_id",
        "title",
        "overview",
        "genres",
        "keywords",
        "cast",
        "crew",
    ]
]

movies.dropna(inplace=True)


def convert(text):
    result = []

    for item in ast.literal_eval(text):
        result.append(item["name"])

    return result


def fetch_cast(text):
    result = []

    for i, item in enumerate(ast.literal_eval(text)):
        if i < 3:
            result.append(item["name"])
        else:
            break

    return result


def fetch_director(text):
    result = []

    for item in ast.literal_eval(text):
        if item["job"] == "Director":
            result.append(item["name"])
            break

    return result


movies["genres"] = movies["genres"].apply(convert)
movies["keywords"] = movies["keywords"].apply(convert)
movies["cast"] = movies["cast"].apply(fetch_cast)
movies["crew"] = movies["crew"].apply(fetch_director)

movies["overview"] = movies["overview"].apply(lambda x: x.split())


def collapse(L):
    return [i.replace(" ", "") for i in L]


movies["genres"] = movies["genres"].apply(collapse)
movies["keywords"] = movies["keywords"].apply(collapse)
movies["cast"] = movies["cast"].apply(collapse)
movies["crew"] = movies["crew"].apply(collapse)

movies["tags"] = (
    movies["overview"]
    + movies["genres"]
    + movies["keywords"]
    + movies["cast"]
    + movies["crew"]
)

new_df = movies[["movie_id", "title", "tags"]]

new_df["tags"] = new_df["tags"].apply(
    lambda x: " ".join(x).lower()
)

cv = CountVectorizer(
    max_features=5000,
    stop_words="english"
)

vectors = cv.fit_transform(
    new_df["tags"]
).toarray()

similarity = cosine_similarity(vectors)

pickle.dump(new_df, open("movies.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))

print("Model created successfully!")