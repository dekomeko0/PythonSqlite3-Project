import sqlite3 as sql

def create_table():
    conn = sql.connect('data.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS(
        id INTEGER PRIMARY KEY,
        name TEXT,
        lastname TEXT,
        username TEXT,
        password TEXT
        )""")
    
    conn.commit()
    conn.close()

def insert(name, lastname, username, password):
    conn = sql.connect('data.db')
    cursor = conn.cursor()
    
    add_command = "INSERT INTO USERS(name, lastname, username, password) VALUES '{}'"
    data = (name, lastname, username, password)
    
    cursor.execute(add_command, data)
    
    conn.commit()
    conn.close()

def print_all():
    conn = sql.connect('data.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM USERS")
    list_all = cursor.fetchall()
    
    conn.close()
    return list_all

def search_username(username):
    conn = sql.connect('data.db')
    cursor = conn.cursor()
    
    search_command = "SELECT * FROM USERS WHERE username = ?"
    cursor.execute(search_command, (username,))
    
    user = cursor.fetchone()
    
    conn.close()
    return user

def password_update(username, new_password):
    conn = sql.connect('data.db')
    cursor = conn.cursor()
    
    upd_command = "UPDATE USERS SET password = ? WHERE username = ?"
    cursor.execute(upd_command, (new_password, username))
    
    conn.commit()
    conn.close()

def delete_user(username):
    conn = sql.connect('data.db')
    cursor = conn.cursor()
    
    delete_command = "DELETE FROM USERS WHERE username = ?"
    cursor.execute(delete_command, (username,))
    
    conn.commit()
    conn.close()
