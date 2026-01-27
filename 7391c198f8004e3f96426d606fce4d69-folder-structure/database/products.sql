CREATE TABLE IF NOT EXISTS product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL UNIQUE,
    price FLOAT NOT NULL,
    description VARCHAR(500) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL UNIQUE,
    parent_id INT NULL,
    FOREIGN KEY(parent_id) REFERENCES category(id)
);

CREATE TABLE IF NOT EXISTS product_category (
    product_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY(product_id, category_id),
    FOREIGN KEY(product_id) REFERENCES product(id),
    FOREIGN KEY(category_id) REFERENCES category(id)
);