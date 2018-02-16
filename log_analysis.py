#!/usr/bin/env python3

import sys
import psycopg2


def connect(DBNAME):
    """Connect to the PostgreSQL database. Returns a database connection"""
    try:
        db = psycopg2.connect("dbname={}".format(DBNAME))
        cursor = db.cursor()
        return db, cursor
    except psycopg2.Error as e:
        print("Unable to connect to database")
        sys.exit(1)


def run_query(query, db, cursor):
    """run_query: running a query with psql using psycopg2"""
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results


def result_text(question, results, col2):
    """result_text: prints questions and results in plain text"""
    print('')
    print(question)
    print('')
    for ii, i in enumerate(results, 1):
        print('     {})  {} ---- {} {}'.format(ii, i[0], i[1], col2))
    print('')

# List of questions + queries


question_1 = "1. What are the most popular three articles of all time? "

query_1 = '''
        SELECT distinct articles.title, total_views.views
        FROM (
            SELECT log.path, count(*) AS views
            FROM log
            GROUP BY path
        ) AS total_views
        INNER JOIN articles
        ON total_views.path = '/article/' || articles.slug
        ORDER BY views DESC
        LIMIT 3;
'''
question_2 = "2. Who are the most popular article authors of all time?"

query_2 = '''
        SELECT authors_articles.name,
        SUM(total_views.views) AS views
        FROM (
            SELECT regexp_replace(log.path, '/article/', '', 'g') AS slug,
            COUNT(log.path) AS views
            FROM log
            GROUP BY path
        ) AS total_views,
            (
            SELECT distinct articles.slug, authors.name
            FROM articles JOIN authors
            ON authors.id = articles.author
        ) AS authors_articles
        WHERE authors_articles.slug = total_views.slug
        GROUP BY name
        ORDER BY views DESC
        LIMIT 3;
'''

question_3 = "3. On which days did more than 1% of requests lead to errors?"

query_3 = '''
        SELECT to_char(MDY, 'FMMonth DD, YYYY'), fail_table.fail_per
        FROM (
            SELECT round(SUM(CASE WHEN status = '404 NOT FOUND' THEN 1 END)
            * 100.0/ COUNT(log.status),2) AS fail_per,
            time::date AS MDY
            FROM log
            GROUP BY MDY
        ) AS fail_table
        WHERE fail_per >= 1
'''

# Main Function: Running queries and fetching the results


if __name__ == "__main__":
    DBNAME = "news"
    db, cursor = connect(DBNAME)
    results_1 = run_query(query_1, db, cursor)
    result_text(question_1, results_1, 'views')
    results_2 = run_query(query_2, db, cursor)
    result_text(question_2, results_2, 'views')
    results_3 = run_query(query_3, db, cursor)
    result_text(question_3, results_3, "%")
    db.close()
