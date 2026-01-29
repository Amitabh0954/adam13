# Epic Title: User Account Management

CREATE TABLE failed_attempts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);