DROP TABLE IF EXISTS inventory_test;

CREATE TABLE inventory_test (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  sell_in INTEGER,
  quality INTEGER
);