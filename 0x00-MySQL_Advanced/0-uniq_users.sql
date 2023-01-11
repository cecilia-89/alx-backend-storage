-- Creates a Table Users with some requirements
-- Creates table users if it doesn't exits don't throw error
CREATE TABLE Users (id INT NOT NULL PRIMARY KEY,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    name VARCHAR(255)) IF NOT EXISTS;

