ALTER TABLE products ADD COLUMN is_deleted BOOLEAN DEFAULT FALSE;

#### 7. Ensure this feature works by initializing it in the application