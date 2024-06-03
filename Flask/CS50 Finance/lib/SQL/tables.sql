CREATE TABLE IF NOT EXISTS users (
    -- The user table
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    cash NUMERIC(2) NOT NULL DEFAULT 10000.00,
    stock_value NUMERIC(2) NOT NULL DEFAULT 0.00,
    total NUMERIC(2) NOT NULL DEFAULT 0.00,

    --  Constraints ( Rules which should apply)
    UNIQUE(username);

)

CREATE TABLE IF NOT EXISTS ? (

    --  User's Trading portefolio
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    abbrivation TEXT NOT NULL,
    qty INT NOT NULL,
    price REAL NOT NULL,
    total REAL NOT NULL,
    UNIQUE (abbrivation));

CREATE TABLE trading_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                user_id INTEGER NOT NULL,
                                abbrivation TEXT NOT NULL,
                                status TEXT NOT NULL DEFAULT UNKOWN,
                                qty INT NOT NULL,
                                price REAL NOT NULL,
                                time_stamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                                FOREIGN KEY (user_id) REFERENCES users(id));
