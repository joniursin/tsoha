DROP TABLE restaurants CASCADE;
DROP TABLE users CASCADE;
DROP TABLE reviews CASCADE;
CREATE TABLE restaurants (id SERIAL PRIMARY KEY, name TEXT);
CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT, op_status BOOLEAN);
CREATE TABLE reviews (id SERIAL PRIMARY KEY, restaurant_id INTEGER REFERENCES restaurants, user_id INTEGER REFERENCES users, username TEXT, rating INT, content TEXT, created_at TIMESTAMP);
INSERT INTO restaurants (name) VALUES ('Dilber');
INSERT INTO restaurants (name) VALUES ('King Kebab');
INSERT INTO restaurants (name) VALUES ('Hesburger');