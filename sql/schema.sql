PRAGMA foreign_keys = ON;

CREATE TABLE friends(
  name VARCHAR(20) NOT NULL,
  connection VARCHAR(40) NOT NULL,
  PRIMARY KEY(name)
);
