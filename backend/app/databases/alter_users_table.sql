ALTER TABLE users ADD COLUMN login_attempts INT DEFAULT 0, ADD COLUMN last_login_attempt DATETIME, ADD COLUMN is_active BOOLEAN DEFAULT TRUE;

#### 7. Ensure this feature works by initializing it in the application

##### Initialize Application with Updated Models and Routes