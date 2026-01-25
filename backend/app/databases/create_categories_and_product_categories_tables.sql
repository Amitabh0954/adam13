CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    parent_id INT,
    FOREIGN KEY (parent_id) REFERENCES categories(id)
);

CREATE TABLE product_categories (
    product_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

#### 8. Ensure this feature works by initializing it in the application