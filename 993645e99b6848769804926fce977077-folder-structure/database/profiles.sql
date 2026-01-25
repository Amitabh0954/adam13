CREATE TABLE profiles (
    user_id INT NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    preferences JSON,
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);