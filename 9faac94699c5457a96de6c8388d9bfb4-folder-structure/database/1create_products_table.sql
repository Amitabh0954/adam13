# Epic Title: Product Catalog Management

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL CHECK (price > 0)
);