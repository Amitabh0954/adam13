CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL UNIQUE,
    description VARCHAR(500) NOT NULL,
    price FLOAT NOT NULL CHECK (price > 0),
    category VARCHAR(50) NULL,
    attributes VARCHAR(500) NULL,   -- Combined attributes as a JSON string
    is_deleted BOOLEAN NOT NULL DEFAULT FALSE
);