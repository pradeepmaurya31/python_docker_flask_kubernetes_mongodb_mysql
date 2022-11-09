CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Auth123';

CREATE database auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

use auth;

CREATE TABLE user(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(250) NOT NULL
);

INSERT INTO user(email, password) VALUES('pradeep@gmail.com', 'pradeep@123');