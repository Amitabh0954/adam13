CREATE TABLE carts (
    user_id INT NOT NULL,
    items JSON NOT NULL,
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);