import psycopg2
import sqlalchemy

db = 'postgresql://postgres:36626688@localhost:5432/postgres'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

request1 = connection.execute("SELECT name, year FROM album WHERE year = 2018;").fetchall()
request2 = (connection.execute("SELECT name, duration FROM song ORDER BY duration;").fetchall())[-1]
request3 = connection.execute("SELECT name, duration FROM song WHERE duration >= '3.30';").fetchall()
request4 = connection.execute("SELECT name FROM collection WHERE year BETWEEN 2018 AND 2020;").fetchall()
request5 = connection.execute("SELECT name FROM singer WHERE name NOT LIKE '%% %%';").fetchall()
request6 = connection.execute("SELECT name FROM song WHERE name LIKE '%%my%%';").fetchall()
