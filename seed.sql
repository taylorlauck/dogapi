
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  date_made DATE NOT NULL
);

CREATE TABLE breeds (
  id SERIAL PRIMARY KEY,
   dogs_picked TEXT NOT NULL 
);

CREATE TABLE pickedbreeds (
  id SERIAL PRIMARY KEY,
  users_id INTEGER REFERENCES users ON DELETE CASCADE,
  breeds_id INTEGER REFERENCES breeds ON DELETE CASCADE
);






