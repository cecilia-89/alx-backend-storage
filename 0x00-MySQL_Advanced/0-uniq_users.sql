-- Creates a Table Users with some requirements
-- Creates table users if it doesn't exits don't throw error
CREATE TABLE Users (
  id INT,
  email VARCHAR(255),
  name VARCHAR(255),
  PRIMARY KEY(id)
);
