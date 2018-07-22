# "Database code" for the DB News.

import datetime
import psycopg2
import bleach


def get_most_popular_articles(conn):
    """Return three most accessed articles of all time,
    sorted list with the most popular article at the top."""
    c = conn.cursor()
    c.execute("select * from most_popular_articles")
    articles = c.fetchall()
    print ("1. What are the most popular three articles of all time?")
    for row in articles:
        print ("\"" + row[0] + "\" - " + str(row[1]) + " views")
    return articles


def get_most_popular_article_authors(conn):
    """Return authors who got the most page views,
    sorted list with the most popular author at the top."""
    c = conn.cursor()
    c.execute("select * from most_popular_article_authors")
    authors = c.fetchall()
    print ("2. Who are the most popular article authors of all time?")
    for row in authors:
        print ("\"" + row[0] + "\" - " + str(row[1]) + " views")
    return authors


def get_erroneous_req_per_day_gt_a_percent(conn):
    """Return day and error rate in percent for the days when
    more than 1% of requests lead to errors."""
    c = conn.cursor()
    c.execute("select * from erroneous_requests_per_day_more_than_a_percent")
    erroneous_requests = c.fetchall()
    print ("3. On which days did more than 1% of requests lead to errors?")
    for row in erroneous_requests:
        print (row[0].strftime("%b %d, %Y") + " - " + str(row[1]) + "%")
    return erroneous_requests

DBNAME = "news"
db = psycopg2.connect("dbname=" + DBNAME)
print ("--Analyzing Logs--")
most_popular_articles = get_most_popular_articles(db)
most_popular_article_authors = get_most_popular_article_authors(db)
erroneous_req_per_day_gt_a_percent = get_erroneous_req_per_day_gt_a_percent(db)
print ("--Logs Analysis Complete--")
db.close()
