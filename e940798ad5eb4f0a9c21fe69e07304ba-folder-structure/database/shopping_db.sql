# Epic Title: Shopping Cart Functionality

CREATE DATABASE IF NOT EXISTS shopping_db;
USE shopping_db;

CREATE TABLE IF NOT EXISTS shopping_cart (
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (user_id, product_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);