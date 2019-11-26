-- Convert db , table and field to utf-8
-- Enter the hbtn_0c_0 database
USE hbtn_0c_0
-- Convert database to utf-8
ALTER DATABASE hbtn_0c_0  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Convert table to utf-8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;