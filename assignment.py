# Database code for the DB Forum, full solution!

import psycopg2,datetime

DBNAME = "news"
formatStr = '%b %d, %Y'
sqlDateFormat = '%Y-%m-%d'
def get_popular_articles():
  """the most popular three articles of all time"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select articles.id,articles.title, count(*) as views from articles join log on log.path=CONCAT('/article/',articles.slug) group by articles.id,articles.title order by views desc limit 3;")
  # print"The most popular articles of all time are:"
  for row in c:
    print"\"{}\" - {} views".format(row[1],row[2])
  db.close()

# view schema article_author
# create view article_author as (select articles.id as articleId, articles.slug as articleSlug, articles.title as articleTitle, authors.id as authorId, authors.name as authorName from articles join authors on articles.author = authors.id);

def most_popular_authors():
  """the most popular article authors of all time"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select article_author.authorName, count(*) as views from article_author join log on log.path=CONCAT('/article/',article_author.articleSlug) group by article_author.authorId, article_author.authorName order by views desc limit 3")
  # print"The most popular authors of all time are:"
  for row in c:
    print"{} - {} views".format(row[0],row[1])
  db.close()

# date_wise_failed_request
# create view date_wise_failed_request as select cast(time as DATE) as date, count(*) as failures from log where status != '200 OK' group by cast(time as DATE) order by failures desc;

# date_wise_request
# create view date_wise_request as select cast(time as DATE) as date, count(*)  from log group by cast(time as DATE);
def error_more_than_one_percent():
  """On which days did more than 1% of requests lead to errors"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select TO_CHAR(date_wise_failed_request.date,'Mon DD, YYYY') as dateStr, ROUND((date_wise_failed_request.failures * 100/date_wise_request.count),2) as failure_rate from date_wise_request join date_wise_failed_request on date_wise_failed_request.date = date_wise_request.date")
  # print"The days with error rate more than 1 percent:"
  for row in c:
    date = row[0]
    failure_rate = row[1]
    # views = row[2]
    # print("{} views {} failures".format(views, failures))
    # errorPercent = round((float(failures)/views)*100, 2);
    if(failure_rate > 1):
      print("{} - {} %".format(date , failure_rate))
  db.close()

if __name__ == '__main__':
  print"The most popular articles of all time are:"
  get_popular_articles()
  print"\nThe most popular authors of all time are:"
  most_popular_authors();
  print"\nThe days with error rate more than 1 percent:"
  error_more_than_one_percent();

