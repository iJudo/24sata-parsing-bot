import sqlite3

conn = sqlite3.connect("news.sqlite3")
cursor = conn.cursor()
def init_db():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS NEWS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            IMG TEXT NOT NULL,
            TITLE TEXT NOT NULL,
            LINK TEXT NOT NULL UNIQUE,
            DESCRIPTION TEXT NOT NULL,
            IS_SENT INTEGER NOT NULL DEFAULT 0
        )
        
                   """)

def insert_news(img,title,link,description):
    cursor.execute("""
    insert or ignore into NEWS (img,title,link,description) values (?,?,?,?)
    """, (img,title,link,description))
    conn.commit()

def get_unsent_news():
    cursor.execute("""
        SELECT id, img, title, link, description FROM NEWS WHERE IS_SENT = 0
        
    """)
    return cursor.fetchall()

def mark_as_sent(id):
    cursor.execute(""" 
    UPDATE NEWS SET IS_SENT = 1
    WHERE id = ?""",(id,))
    conn.commit()