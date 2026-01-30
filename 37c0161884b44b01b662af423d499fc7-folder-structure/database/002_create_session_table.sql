# Epic Title: User Login

CREATE TABLE session (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    session_id VARCHAR(255) NOT NULL UNIQUE,
    created_at DATETIME NOT NULL,
    last_activity DATETIME NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(id)
);