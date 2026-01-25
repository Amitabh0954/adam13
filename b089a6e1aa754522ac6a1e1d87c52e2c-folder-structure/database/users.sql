CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    first_name VARCHAR(50) NULL,
    last_name VARCHAR(50) NULL,
    date_of_birth DATETIME NULL,
    address VARCHAR(255) NULL,
    city VARCHAR(50) NULL,
    country VARCHAR(50) NULL,
    phone_number VARCHAR(20) NULL,
    failed_login_attempts INT NOT NULL DEFAULT 0,
    account_locked_until DATETIME NULL
);

CREATE TABLE password_reset_tokens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    token VARCHAR(128) NOT NULL,
    created_at DATETIME NOT NULL,
    expires_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);