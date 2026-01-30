# Epic Title: Profile Management

CREATE TABLE profile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    date_of_birth DATE,
    updated_at DATETIME NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(id)
);