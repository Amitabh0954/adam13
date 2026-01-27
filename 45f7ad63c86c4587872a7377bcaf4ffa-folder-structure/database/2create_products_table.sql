# Epic Title: Product Catalog Management

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE,
    category VARCHAR(200) NOT NULL,
    attributes TEXT NOT NULL,
    price FLOAT NOT NULL,
    description TEXT NOT NULL
);