CREATE TABLE portefolio IF NOT EXISTS (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    tag TEXT NOT NULL,
    url TEXT NOT NULL,
    gurl TEXT NOT NULL,
    yurl TEXT NOT NULL,
    dato DATETIME NOT NULL DEFAULT DATE
);

CREATE TABLE cookies IF NOT EXISTS (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    txtfile BLOB NOT NULL,
    dato TIMESTAMP NOT NULL,
)