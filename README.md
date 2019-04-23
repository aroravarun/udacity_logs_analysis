# udacity_logs_analysis

Description:
The project serves as a logging tool for a news website.
It exposes 3 functionalities:
* Get the 3 top most read articles on the website
* Get the 3 top most read authors on the website
* Get the days on which error rate was more than 1 percent

Setup:

Virtual Machine Setup
You need to setup a vagrant iirtual machine to set it up.
The steps to setup it up are as follows:
1.) Download the latest Virtual Box which is compatible with vagrant from the link:
https://www.virtualbox.org/wiki/Download_Old_Builds_5_1

2.) Download and install vagrant from the below mentioned link as per your system platform
https://www.vagrantup.com/downloads.html

3.) Change directory to vagrant and execute "vagrant up". It will download the required files for settings up the virtual machine.
4.) Execute "vagrant ssh"

Database Setup:
1.) Download the newsdata.sql from the below mentiond:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

2.) Unzip newsdata.zip to get the newsdata.sql

3.) To access and load the data, cd into the vagrant directory and use the command 
"psql -d news -f newsdata.sql"
4.) Create Views using the following sql queries on the news database:
  * create view article_author as (select articles.id as articleId, articles.slug as articleSlug, articles.title as articleTitle, authors.id as authorId, authors.name as authorName from articles join authors on articles.author = authors.id);

  * create view date_wise_failed_request as select cast(time as DATE) as date, count(*) as failures from log where status != '200 OK' group by cast(time as DATE) order by failures desc;

  * create view date_wise_request as select cast(time as DATE) as date, count(*)  from log group by cast(time as DATE);


Project Execution:

1.) Execute the following command:
python news_logs_analysis/assignment.py
