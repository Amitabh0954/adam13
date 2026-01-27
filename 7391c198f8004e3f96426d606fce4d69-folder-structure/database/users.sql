CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    last_login_at DATETIME DEFAULT NULL,
    current_login_at DATETIME DEFAULT NULL,
    login_count INT DEFAULT 0 NOT NULL,
    first_name VARCHAR(50) DEFAULT NULL,
    last_name VARCHAR(50) DEFAULT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    invalid_login_attempts INT DEFAULT 0 NOT NULL
);