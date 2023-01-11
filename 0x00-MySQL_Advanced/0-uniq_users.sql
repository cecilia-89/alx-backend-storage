-- Creates a Table Users with some requirements
-- Creates table users if it doesn't exits don't throw error
CREATE TABLE Users (
  id int NOT NULL,
  email varchar(255) NOT NULL,
  name varchar(255),
  PRIMARY KEY(id)
) IF NOT EXISTS;
