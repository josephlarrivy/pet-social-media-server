DROP TABLE IF EXISTS pets CASCADE;
DROP TABLE IF EXISTS pet_types CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
  id VARCHAR(35) PRIMARY KEY NOT NULL,
  email VARCHAR(70) NOT NULL,
  owner_name VARCHAR(50) NOT NULL,
  avatar VARCHAR(300) NOT NULL,
  password_hash VARCHAR(100) NOT NULL,
  initialization_date_time DATE NOT NULL,
  login_count INTEGER NOT NULL,
  last_login DATE
);

CREATE TABLE pet_types (
  id VARCHAR(35) PRIMARY KEY NOT NULL,
  type_name VARCHAR(50) NOT NULL
);

CREATE TABLE pets (
  id VARCHAR(35) PRIMARY KEY NOT NULL,
  owner_id VARCHAR(35) NOT NULL,
  type_id VARCHAR(35) NOT NULL,
  name VARCHAR(50) NOT NULL,
  avatar VARCHAR(300) NOT NULL,
  initialization_date_time DATE NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES users (id) ON DELETE CASCADE,
  FOREIGN KEY (type_id) REFERENCES pet_types (id) ON DELETE SET NULL
);

INSERT INTO users (id, email, owner_name, avatar, password_hash, initialization_date_time, login_count, last_login)
VALUES ('user_1', 'user_1@example.com', 'User One', 'user_avatar', 'user_password', '2023-07-06', 0, NULL);

INSERT INTO pet_types (id, type_name) VALUES 
('type_1', 'dog'),
('type_2', 'cat'),
('type_3', 'fish'),
('type_4', 'bird'),
('type_5', 'hamster'),
('type_6', 'rabbit'),
('type_7', 'snake');