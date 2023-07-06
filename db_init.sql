DROP TABLE IF EXISTS users CASCADE;

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
