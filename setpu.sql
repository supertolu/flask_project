CREATE DATABASE flask_assignment;

USE flask_assignment;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(150),
    age INT,
    city VARCHAR(100),
    country VARCHAR(100),
    occupation VARCHAR(100),
    hobby VARCHAR(150),
    programming_language VARCHAR(50),
    online_hours INT,
    entertainment VARCHAR(100)
);