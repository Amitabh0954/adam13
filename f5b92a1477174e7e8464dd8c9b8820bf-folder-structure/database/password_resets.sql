CREATE TABLE password_resets (
    token VARCHAR(120) PRIMARY KEY,
    user_id INT NOT NULL,
    expiry DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);