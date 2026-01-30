# Epic Title: Product Categorization

CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    parent_id INT,
    FOREIGN KEY(parent_id) REFERENCES category(id)
);