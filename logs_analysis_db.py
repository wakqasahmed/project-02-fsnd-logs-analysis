# "Database code" for the DB News.

import datetime
import psycopg2
import bleach

DBNAME = "news"


def get_most_popular_articles():
    """Return three most accessed articles of all time,
    sorted list with the most popular article at the top."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select * from most_popular_articles")
    articles = c.fetchall()
    db.close()
    return articles


def get_most_popular_article_authors():
    """Return authors who got the most page views,
    sorted list with the most popular author at the top."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select * from most_popular_article_authors")
    authors = c.fetchall()
    db.close()
    return authors


def get_erroneous_requests_per_day_gt_a_percent():
    """Return day and error rate in percent for the days when
    more than 1% of requests lead to errors."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select * from erroneous_requests_per_day_more_than_a_percent")
    erroreneous_requests = c.fetchall()
    db.close()
    return erroreneous_requests
