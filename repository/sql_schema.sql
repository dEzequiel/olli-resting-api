DROP TABLE IF EXISTS inventory;

CREATE TABLE inventory (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  sell_in INTEGER,
  quality INTEGER
);