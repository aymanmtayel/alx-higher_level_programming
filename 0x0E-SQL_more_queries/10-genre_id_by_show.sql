-- script that lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
SELECT shows.title, genres.show_id
FROM tv_show_genres genres LEFT JOIN tv_shows shows
ON genres.show_id = shows.id
ORDER BY shows.title, genres.genre_id ASC;
