# Project: Logs Analysis
This project is part of the Full Stack Developer Nanodegree Program at Udacity. It analyses the logs of news database and answers a couple of important questions.

More details can be found here:

**[Project Overview](./project_overview.md)**

**[Project Details](./project_details.md)**

**[Project Submission](./project_submission.md)**

**[Logs Analysis Result in Plain Text](./logs_analysis_result.txt)**

# How to run?

## Pre-requisites
- Python 2.7.12
- PSQL 9.5.13
- Web Browser (Recommended: Chrome)
- Internet Connection (its not offline compatible)
- A bit of Curosity ;)
- Prepare the [software and data](./project_details.md#prepare-the-software-and-data)

## Run
- `clone` or `download` the code in your `vagrant` folder
- [SSH into vagrant](./project_details.md#the-virtual-machine) using `vagrant ssh`

### Step 1: Create the views
- Enter the database using `psql news`
- Run the following commands (ignore the warnings but make sure after it is run, it says **CREATE VIEW**):
```
CREATE OR REPLACE VIEW most_popular_articles AS (
	SELECT a.title, COUNT(l.*) AS views
	FROM articles a, log l
	WHERE l.path LIKE '%' || a.slug
	GROUP BY a.title
	ORDER BY views DESC LIMIT 3
);

CREATE OR REPLACE VIEW most_popular_article_authors AS (
	SELECT most_views.author_name, SUM(most_views.article_views) AS views FROM
	(SELECT au.name AS author_name, COUNT(l.path) AS article_views
	FROM articles ar
	JOIN authors au ON au.id = ar.author
	LEFT JOIN log l ON l.path LIKE '%' || ar.slug
	GROUP BY au.name) AS most_views
	GROUP BY most_views.author_name
	ORDER BY views DESC
);

CREATE OR REPLACE VIEW erroneous_requests_per_day_more_than_a_percent AS (
	SELECT critical_error_log.day, ROUND(critical_error_log.request_to_error_ratio,1) as request_to_error_ratio
	FROM
	(
		SELECT error_log.day,
		SUM(error_log.no_of_errors)/SUM(error_log.no_of_requests)*100 AS request_to_error_ratio,
		SUM(error_log.no_of_requests) AS total_requests,
		SUM(error_log.no_of_errors) AS total_errors
		FROM
		(
			SELECT time::date AS day, COUNT(status) AS no_of_requests, '0' AS no_of_errors 
			FROM log
			GROUP BY day

			UNION

			SELECT time::date AS day, '0' AS no_of_requests, COUNT(status) AS no_of_errors
			FROM log
			WHERE status != '200 OK'
			GROUP BY day
			) AS error_log
		GROUP BY error_log.day
	)
	AS critical_error_log
	WHERE critical_error_log.request_to_error_ratio > 1
);

```
- Now you can run the following queries to get the logs analysis:
  1. What are the most popular three articles of all time? `SELECT * FROM most_popular_articles;`
  2. Who are the most popular article authors of all time? `SELECT * FROM most_popular_article_authors;`
  3. On which days did more than 1% of requests lead to errors? `SELECT * FROM erroneous_requests_per_day_more_than_a_percent;`

### Step 2: Run the analysis (**BONUS**)
- Run `logs_analysis.py` using the following command: `python logs_analysis.py`
- Browse to `http://0.0.0.0:8000`
- Done - You should see web browser displaying the logs analysis and HTTP request logging in terminal

# Technology Stack
This website uses the following technologies:
- **Python 2.7.12**
- **PSQL 9.5.13**

# Issues
- Feel free to report if you find any

# License
This project is a public domain work, dedicated using CC0 1.0. Feel free to do whatever you want with it. (If you are a udacity student, learn but not cheat :P)
