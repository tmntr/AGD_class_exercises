import sqlite3

create_users_table = """
CREATE TABLE IF NOT EXISTS user (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
gender TEXT,
nationality TEXT
);
"""

create_posts_table = """
CREATE TABLE IF NOT EXISTS post (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
description TEXT NOT NULL,
user_id INTEGER NOT NULL,
FOREIGN KEY (user_id) REFERENCES user (id)
);
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS like (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
post_id INTEGER NOT NULL,
FOREIGN KEY (user_id) REFERENCES user (id),
FOREIGN KEY (post_id) REFERENCES post (id)
);
"""

create_comments_table = """
CREATE TABLE IF NOT EXISTS comment (
id INTEGER PRIMARY KEY AUTOINCREMENT,
content TEXT NOT NULL,
user_id INTEGER NOT NULL,
post_id INTEGER NOT NULL,
FOREIGN KEY (user_id) REFERENCES user (id),
FOREIGN KEY (post_id) REFERENCES post (id)
);
"""

with sqlite3.connect('soziales_medien.sqlite') as conn:
    cursor = conn.cursor()

    cursor.execute(create_users_table)
    cursor.execute(create_posts_table)
    cursor.execute(create_likes_table)
    cursor.execute(create_comments_table)

    conn.commit()
