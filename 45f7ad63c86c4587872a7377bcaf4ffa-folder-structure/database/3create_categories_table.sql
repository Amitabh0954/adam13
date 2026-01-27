# Epic Title: Product Catalog Management

CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE,
    parent_id INT,
    CONSTRAINT fk_parent_category FOREIGN KEY (parent_id) REFERENCES categories(id)
);