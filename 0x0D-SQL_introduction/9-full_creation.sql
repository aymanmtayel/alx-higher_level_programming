-- creates a second table in my database and the database is argument
-- usage mysql -hlocalhost -uuser -p <database>
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score) VALUES (1, "JOHN", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);
