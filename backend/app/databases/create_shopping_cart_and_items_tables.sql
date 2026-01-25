CREATE TABLE shopping_carts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    session_id VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE shopping_cart_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cart_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    price FLOAT NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES shopping_carts(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

#### 7. Ensure this feature works by initializing it in the application