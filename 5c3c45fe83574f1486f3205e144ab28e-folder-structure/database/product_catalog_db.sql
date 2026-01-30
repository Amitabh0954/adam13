# Epic Title: Product Catalog Management
-- Adding categories to the schema for product categorization

CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    parent_id INT,
    FOREIGN KEY (parent_id) REFERENCES categories(id) ON DELETE CASCADE
);

ALTER TABLE products
ADD COLUMN category_id INT,
ADD FOREIGN KEY (category_id) REFERENCES categories(id);