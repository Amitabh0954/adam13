# Epic Title: Product Catalog Management

CREATE DATABASE IF NOT EXISTS product_db;
USE product_db;

CREATE TABLE IF NOT EXISTS products (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT NOT NULL,
    PRIMARY KEY (id)
);