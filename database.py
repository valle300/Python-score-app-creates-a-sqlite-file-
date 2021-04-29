#database.py
#Erick Valle
#02/26/2021

import sqlite3

CREATE_SCORES_TABLE = "CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, gender TEXT, score INTEGER);"

INSERT_SCORE = "INSERT INTO scores (name, age, gender, score) VALUES (?, ?, ?, ?);"

GET_ALL_SCORES = "SELECT * FROM scores;"
GET_SCORES_BY_NAME = "SELECT * FROM scores WHERE name = ?;"
GET_HIGHEST_SCORE_FOR_SCORES = """
SELECT * FROM scores
ORDER BY score DESC
LIMIT 1;"""


def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_SCORES_TABLE)

def add_score(connection, name, age, gender, score):
    with connection:
        connection.execute(INSERT_SCORE, (name, age, gender, score))

def get_all_scores(connection):
    with connection:
        return connection.execute(GET_ALL_SCORES)


def get_scores_by_name(connection, name):
    with connection:
        return connection.execute(GET_SCORES_BY_NAME, (name,)).fetchall()


def get_highest_score_for_scores(connection):
    with connection:
        return connection.execute(GET_HIGHEST_SCORE_FOR_SCORES).fetchone()
