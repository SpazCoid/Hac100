import sqlite3

conn=sqlite3.connect("News.db")

conn.execute('''Create Table IF NOT EXISTS News
             (Title                     TEXT  (50) NOT NULL,
              Description               TEXT (50)            NOT NULL,
              URL                       TEXT (50)           NOT NULL,
              publishedAt               TEXT (15)           NOT NULL,
              Content                   TEXT (500)           NOT NULL,
              Sent                      Boolean(1)           NOT NULL,
              PRIMARY KEY (Title)
              UNIQUE(Title,URL)
              );''')
