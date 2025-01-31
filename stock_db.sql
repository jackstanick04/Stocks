-- need to only create if it doesnt exist or it will try and make new table every time file is ran
CREATE TABLE IF NOT EXISTS test (
    name TEXT
);

-- just inserting values
INSERT INTO test (name)
VALUES ('Jack');


