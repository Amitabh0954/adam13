CREATE TABLE IF NOT EXISTS password_reset_token (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    token VARCHAR(100) NOT NULL UNIQUE,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
);