# udacity_logs_analysis


Views create SQL queries:

1.) create view article_author as (select articles.id as articleId, articles.slug as articleSlug, articles.title as articleTitle, authors.id as authorId, authors.name as authorName from articles join authors on articles.author = authors.id);

2.) create view date_wise_failed_request as select cast(time as DATE) as date, count(*) as failures from log where status != '200 OK' group by cast(time as DATE) order by failures desc;

3.) create view date_wise_request as select cast(time as DATE) as date, count(*)  from log group by cast(time as DATE);


Execution command:

python assignment.py