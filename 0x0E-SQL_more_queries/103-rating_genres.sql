-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT a.name, sum(c.rate) AS rating FROM tv_genres a 
RIGHT JOIN tv_show_genres b
ON a.id = b.genre_id
LEFT JOIN tv_show_ratings c
ON c.show_id = b.show_id
GROUP BY 1
ORDER BY 2 DESC;
