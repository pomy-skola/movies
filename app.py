from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DB_PATH = "movies.db"


# ─────────────────────────────────────────────
#  Helper: open a database connection
# ─────────────────────────────────────────────
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # lets you access columns by name, e.g. row["title"]
    return conn


# ─────────────────────────────────────────────
#  Helper: fetch distinct values for dropdowns
# ─────────────────────────────────────────────
def get_filter_options():
    conn = get_db_connection()

    # TODO 1: Write a query that returns every distinct genre, sorted A→Z.
    #         Store the results in `genres`.
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT genre FROM movies ORDER BY genre ASC")
    genres = [row[0] for row in cursor.fetchall()]

    # TODO 2: Write a query that returns every distinct director, sorted A→Z.
    #         Store the results in `directors`.
    cursor.execute("SELECT DISTINCT director FROM movies ORDER BY director ASC")
    directors = [row[0] for row in cursor.fetchall()]

    conn.close()
    return genres, directors


# ─────────────────────────────────────────────
#  Main route
# ─────────────────────────────────────────────
@app.route("/", methods=["GET"])
def index():
    # --- Read filter values sent by the HTML form --------------------------------
    search    = request.args.get("search",   "").strip()
    genre     = request.args.get("genre",    "")
    director  = request.args.get("director", "")
    year_min  = request.args.get("year_min",   type=int, default=1970)
    year_max  = request.args.get("year_max",   type=int, default=2024)
    rating_min = request.args.get("rating_min", type=float, default=0.0)
    rating_max = request.args.get("rating_max", type=float, default=10.0)

    # --- Build the SQL query dynamically -----------------------------------------
    #
    # We use a list of WHERE clauses and a matching list of parameter values.
    # This is the safe way to handle user input — never build SQL by joining
    # strings with user data directly!
    #
    # Example pattern:
    #   conditions = ["year >= ?", "year <= ?"]
    #   params     = [1990, 2010]
    #   WHERE clause becomes: WHERE year >= ? AND year <= ?

    query      = "SELECT * FROM movies"
    conditions = []
    params     = []

    # TODO 3: If `search` is not empty, add a condition that checks whether the
    #         movie title CONTAINS the search text (case-insensitive).
    #         Hint: use LIKE with % wildcards, e.g.  LIKE ?  with value "%text%"
    #         Hint: wrap both sides in UPPER() to make it case-insensitive.
    if search:
        conditions.append("UPPER(title) LIKE ?")
        params.append("%" + search.upper() + "%")

    # TODO 4: If `genre` is not empty, add a condition that matches the genre
    #         exactly (case-insensitive).
    if genre:
        conditions.append("UPPER(genre) = ?")
        params.append(genre.upper())

    # TODO 5: If `director` is not empty, add a condition that matches the
    #         director exactly (case-insensitive).
    if director:
        conditions.append("UPPER(director) = ?")
        params.append(director.upper())

    # TODO 6: Add conditions for year_min, year_max, rating_min, rating_max
    #         so that only movies within those ranges are returned.
    conditions.append("year >= ?")
    params.append(year_min)
    conditions.append("year <= ?")
    params.append(year_max)
    conditions.append("rating >= ?")
    params.append(rating_min)
    conditions.append("rating <= ?")
    params.append(rating_max)

    # Assemble the final query
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " ORDER BY rating DESC"

    # TODO 7: Execute the query with `params` and fetch all results.
    #         Store them in `movies`.
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    movies = cursor.fetchall()
    conn.close()

    genres, directors = get_filter_options()

    return render_template(
        "index.html",
        movies=movies,
        genres=genres,
        directors=directors,
        # Pass filter values back so the form keeps them selected after submit
        search=search,
        selected_genre=genre,
        selected_director=director,
        year_min=year_min,
        year_max=year_max,
        rating_min=rating_min,
        rating_max=rating_max,
        result_count=len(movies),
    )


if __name__ == "__main__":
    app.run(debug=True)
