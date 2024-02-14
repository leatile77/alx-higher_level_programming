-- Creates hbtn_0d_2 database and user_0d_2 user with select privilege and password user_0d_2_pwd
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_d'@'%' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'%';
FLUSH PRIVILEGES;
