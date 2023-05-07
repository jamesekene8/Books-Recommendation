import postgre
import psycopg2 as pg
import pandas.io.sql as psql
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Insert into  postgres database
# postgre.insertingIntoPostgre()

conn = pg.connect(database="amazon",
                  user='postgres', password='342958',
                  host='127.0.0.1', port='5432'
                  )

books = psql.read_sql('SELECT * FROM books', conn)

# querying the database to get the year with more books
books_grouped_year = psql.read_sql(
    'SELECT year, count(title) FROM books GROUP BY year ORDER BY count(year) desc LIMIT 10', conn)

books_2014 = psql.read_sql("SELECT * FROM books WHERE year = '2024'", conn)

highest_priced_pook = psql.read_sql(
    "SELECT * FROM books where price = (SELECT MAX(price) as pm FROM books p)", conn)

books["title"] = books["title"].str.strip()
books["title"] = books["title"].str.lower()

books["index"] = range(0, books.shape[0])

books.set_index("index")

first_column = books.pop('index')

books.insert(0, 'index', first_column)

tfidf = TfidfVectorizer(stop_words='english')
booksVector = tfidf.fit_transform(books['title']).toarray()

cosine_sim = cosine_similarity(booksVector)


def get_recommendations(title):
    idx = books[books['title'] == title.lower()].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(
        sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    book_indices = [i[0] for i in sim_scores]

    return books['title'].iloc[book_indices]


print(get_recommendations("The Light We Carry: Overcoming in Uncertain Times"))
