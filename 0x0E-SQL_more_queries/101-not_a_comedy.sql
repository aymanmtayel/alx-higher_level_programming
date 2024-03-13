-- query to get only the comedy shows
SELECT title FROM tv_shows
WHERE title NOT IN (SELECT a.title FROM tv_shows a LEFT JOIN tv_show_genres b
	ON a.id = b.show_id
	RIGHT JOIN tv_genres c
	ON c.id = b.genre_id WHERE c.name='Comedy')
ORDER BY title ASC;
