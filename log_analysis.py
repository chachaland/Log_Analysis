

import psycopg2


DBNAME = "news"

# run_query: running a query with psql using psycopg2


def run_query(query):
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results
    db.close()

# result_text: prints questions and results in plain text


def result_text(question, results, col2):
    print('')
    print(question)
    print('')
    ii = 1
    for i in results:
        print('     {})  {} ---- {} {}'.format(ii, i[0], i[1], col2))
        ii += 1
    print('')

# List of questions + queries


question_1 = "1. What are the most popular three articles of all time? "

query_1 = '''
        select distinct articles.title, three_top.views from
        (select regexp_replace(log.path, '/article/', '', 'g') as slug,
            count(log.path) as views from log
            group by path
            order by views desc
            limit 3 offset 1) as three_top
        left join articles
        on three_top.slug = articles.slug
        order by views desc;
'''
question_2 = "2. Who are the most popular article authors of all time?"

query_2 = '''
        select authors_articles.name,
        sum(total_views.views) as views from
            (select regexp_replace(log.path, '/article/', '', 'g') as slug,
                count(log.path) as views from log
                group by path) as total_views,
            (select distinct articles.slug, authors.name
                from articles join authors
                on authors.id = articles.author) as authors_articles
        where authors_articles.slug = total_views.slug
        group by name
        order by views desc
        limit 3;
'''

question_3 = "3. On which days did more than 1% of requests lead to errors?"

query_3 = '''
        select fail_table.MDY,fail_table.fail_per from
        (select round(sum(case when status = '404 NOT FOUND' then 1 end)*100.0/
        count(log.status),2) as fail_per,
            to_char(log.time, 'MonthDD,YYYY') as MDY
            from log
            group by MDY) as fail_table
        where fail_per >= 1
'''

# Main Function: Running queries and fetching the results


if __name__ == "__main__":
    results_1 = run_query(query_1)
    result_text(question_1, results_1, 'views')
    results_2 = run_query(query_2)
    result_text(question_2, results_2, 'views')
    results_3 = run_query(query_3)
    result_text(question_3, results_3, "%")
