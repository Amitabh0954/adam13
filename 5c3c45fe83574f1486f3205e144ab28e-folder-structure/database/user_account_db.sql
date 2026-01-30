# Epic Title: User Account Management
-- Additions to the schema for user profile management

ALTER TABLE users
ADD COLUMN first_name VARCHAR(255),
ADD COLUMN last_name VARCHAR(255),
ADD COLUMN preferences TEXT;