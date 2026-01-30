# Epic Title: Shopping Cart Functionality

CREATE DATABASE IF NOT EXISTS shopping_cart_db;
USE shopping_cart_db;

CREATE TABLE IF NOT EXISTS shopping_cart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES product_catalog_db.products(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS saved_carts (
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, product_id),
    FOREIGN KEY (user_id) REFERENCES user_account_db.users(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product_catalog_db.products(id) ON DELETE CASCADE
);