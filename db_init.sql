DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS pets CASCADE;

CREATE TABLE users (
  id VARCHAR(35) PRIMARY KEY NOT NULL,
  email VARCHAR(70) NOT NULL,
  owner_name VARCHAR(50) NOT NULL,
  avatar VARCHAR(300) NOT NULL,
  password_hash VARCHAR(100) NOT NULL,
  initialization_date_time DATE NOT NULL,
  login_count INTEGER NOT NULL,
  last_login DATE NOT NULL
);

CREATE TABLE pets (
  id VARCHAR(35) PRIMARY KEY NOT NULL,
  owner_id VARCHAR(35) NOT NULL REFERENCES users (id),
  name VARCHAR(50) NOT NULL,
  avatar VARCHAR(300) NOT NULL,
  initialization_date_time DATE NOT NULL
);






INSERT INTO users (id, email, owner_name, avatar, password_hash, initialization_date_time, login_count, last_login)
VALUES ('user_1', 'user_1@example.com', 'User One', 'user_avatar', 'user_password', '07-06-23', 0, '07-06-23');