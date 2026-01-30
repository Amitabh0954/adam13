# Epic Title: Add Product to Shopping Cart

CREATE TABLE shopping_cart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE shopping_cart_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cart_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    added_at DATETIME NOT NULL,
    FOREIGN KEY(cart_id) REFERENCES shopping_cart(id),
    FOREIGN KEY(product_id) REFERENCES product(id),
    UNIQUE(cart_id, product_id)
);