# Epic Title: Product Catalog Management

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE,
    category_id INT NOT NULL,
    attributes TEXT NOT NULL,
    price FLOAT NOT NULL,
    description TEXT NOT NULL,
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES categories(id)
);