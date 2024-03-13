-- script that creates A MYSQL user
-- user0d01 with password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;
