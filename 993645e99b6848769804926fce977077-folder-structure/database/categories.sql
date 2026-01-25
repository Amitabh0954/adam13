CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL UNIQUE,
    parent_id INT,
    FOREIGN KEY (parent_id) REFERENCES categories(id)
);