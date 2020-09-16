import sqlite3
from datetime import datetime
i=0
def connect():
    conn=sqlite3.connect("social_media.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    cur.execute("CREATE TABLE  users(id INTEGER PRIMARY KEY ,username text ,created_at text DEFAULT NULL  )")
    cur.execute("CREATE TABLE  photos (id INTEGER PRIMARY KEY,image_url text NOT NULL,user_id INTEGER NOT NULL,created_at TIMESTAMP DEFAULT NULL,FOREIGN KEY(user_id) REFERENCES users(id))")
    cur.execute("CREATE TABLE  comments (id INTEGER  PRIMARY KEY,comment_text text NOT NULL,photo_id INTEGER NOT NULL,user_id INTEGER NOT NULL,created_at TIMESTAMP DEFAULT NULL,FOREIGN KEY(photo_id) REFERENCES photos(id),FOREIGN KEY(user_id) REFERENCES users(id))")
    cur.execute("CREATE TABLE  likes (user_id INTEGER NOT NULL,photo_id INTEGER NOT NULL,created_at TIMESTAMP DEFAULT NULL,FOREIGN KEY(user_id) REFERENCES users(id),FOREIGN KEY(photo_id) REFERENCES photos(id),PRIMARY KEY(user_id, photo_id))")
    cur.execute("CREATE TABLE  follows (follower_id INTEGER NOT NULL,followee_id INTEGER NOT NULL,created_at TIMESTAMP DEFAULT NULL,FOREIGN KEY(follower_id) REFERENCES users(id),FOREIGN KEY(followee_id) REFERENCES users(id),PRIMARY KEY(follower_id, followee_id))")
    cur.execute("CREATE TABLE  tags (id INTEGER PRIMARY KEY,tag_name text UNIQUE,created_at TIMESTAMP DEFAULT NULL)")
    cur.execute("CREATE TABLE  photo_tags (photo_id INTEGER NOT NULL,tag_id INTEGER NOT NULL,FOREIGN KEY(photo_id) REFERENCES photos(id),FOREIGN KEY(tag_id) REFERENCES tags(id),PRIMARY KEY(photo_id, tag_id))")

    conn.commit()
    conn.close()

def user_insert(userid,username):
    conn=sqlite3.connect("social_media.db")
    cur=conn.cursor()
    a=datetime.now()
    a=str(a)
    a=a[:19]
    cur.execute("INSERT INTO users VALUES (?,?,?)",(userid,username,a))
    conn.commit()
    conn.close()
    user_view()

def user_view():
    conn=sqlite3.connect("social_media.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users")
    rows=cur.fetchall()
    conn.close()
    return rows
def photo_insert(photoid,imageurl,pics_userid):
    conn=sqlite3.connect("social_media.db")
    cur=conn.cursor()
    a=datetime.now()
    a=str(a)
    a=a[:19]
    cur.execute("INSERT INTO photos VALUES (?,?,?,?)",(photoid,imageurl,pics_userid,a))
    conn.commit()
    conn.close()
    photo_view()
def photo_view():
    conn=sqlite3.connect("social_media.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM photos")
    rows=cur.fetchall()
    conn.close()
    return rows
def like_insert(userlike,userliked):
    conn=sqlite3.connect("social_media.db")
    cur=conn.cursor()
    a=datetime.now()
    a=str(a)
    a=a[:19]
    cur.execute("INSERT INTO likes VALUES (?,?,?)",(userlike,userliked,a))
    conn.commit()
    conn.close()
    like_view()
def like_view():
    conn=sqlite3.connect("social_media.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM likes")
    rows=cur.fetchall()
    conn.close()
    return rows
def follower_insert(follower,followee):
    conn=sqlite3.connect("social_media.db")
    cur=conn.cursor()
    a=datetime.now()
    a=str(a)
    a=a[:19]
    cur.execute("INSERT INTO follows VALUES (?,?,?)",(follower,followee,a))
    conn.commit()
    conn.close()
    follower_view()
def follower_view():
    conn=sqlite3.connect("social_media.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM follows")
    rows=cur.fetchall()
    conn.close()
    return rows
def comm_insert(commid,comment,cuserid,cpicid):
    conn=sqlite3.connect("social_media.db")
    cur=conn.cursor()
    a=datetime.now()
    a=str(a)
    a=a[:19]
    cur.execute("INSERT INTO comments VALUES (?,?,?,?,?)",(commid,comment,cuserid,cpicid,a))
    conn.commit()
    conn.close()
    comm_view()
def comm_view():
    conn=sqlite3.connect("social_media.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM comments")
    rows=cur.fetchall()
    conn.close()
    return rows
def tag_insert(tagid,tagname):
    conn=sqlite3.connect("social_media.db")
    cur=conn.cursor()
    a=datetime.now()
    a=str(a)
    a=a[:19]
    cur.execute("INSERT INTO tags VALUES (?,?,?)",(tagid,tagname,a))
    conn.commit()
    conn.close()
    comm_view()
def tag_view():
    conn=sqlite3.connect("social_media.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM tags")
    rows=cur.fetchall()
    conn.close()
    return rows


#connect()

