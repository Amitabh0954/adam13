# Epic Title: Product Categorization

CREATE TABLE product_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    category_id INT NOT NULL,
    FOREIGN KEY(product_id) REFERENCES product(id),
    FOREIGN KEY(category_id) REFERENCES category(id)
);