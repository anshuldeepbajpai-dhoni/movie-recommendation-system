from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))


def recommend(movie):

    index = movies[movies["title"] == movie].index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:
        recommendations.append(
            movies.iloc[i[0]].title
        )

    return recommendations

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    if request.method == "POST":

        selected_movie = request.form["movie"]

        recommendations = recommend(selected_movie)

    movie_names = movies["title"].tolist()

    return render_template(
        "index.html",
        movies=movie_names,
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)