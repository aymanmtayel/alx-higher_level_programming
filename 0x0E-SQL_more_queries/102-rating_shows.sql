-- script to get the ratings of the movies
SELECT a.title, SUM(b.rate) AS rating FROM tv_shows a
LEFT JOIN tv_show_ratings b ON a.id = b.show_id 
GROUP BY 1 
ORDER BY 2 DESC;
