--creates a unique table
DROP TABLE IF EXISTS users ;
CREATE TABLE users (
    id INT NOT NULL AUTO INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
