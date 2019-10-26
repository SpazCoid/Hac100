import sqlite3
conn=sqlite3.connect("News.db")
 
conn.execute('''Create Table IF NOT EXISTS News
             (Title                     TEXT NOT NULL,
              Description               TEXT (50)            NOT NULL,
              URL                       TEXT (50)           NOT NULL,
              PublishedAt               TEXT (15)           NOT NULL,
              Content                   TEXT (500)           NOT NULL,
              UNIQUE(Title, PublishedAt),
              PRIMARY KEY (Title)
              );''')

conn.commit()
conn.close()
