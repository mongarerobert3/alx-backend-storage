--creates a unique table
DROP TABLE USERS IF EXISTS;
CREATE TABLE USERS (
    id INT NOT NULL AUTO INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
