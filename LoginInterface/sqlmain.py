from Sqlite3 import *

conn = sql.connect('data.db')
cursor = conn.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS (
        id INTEGER PRIMARY KEY,
        name TEXT,
        lastname TEXT,
        username TEXT,
        password TEXT
        )""")
    conn.commit()

def search_username(username):
    cursor.execute("SELECT * FROM USERS WHERE username = ?", (username,))
    user = cursor.fetchone()
    return user

def insert(name, lastname, username, password):
    cursor.execute("INSERT INTO USERS (name, lastname, username, password) VALUES (?, ?, ?, ?)",
                   (name, lastname, username, password))
    conn.commit()

def printmenu():
    print("""MENÜ:
          1- Giriş
          2- Kayıt ol
          3- Programı Sonlandır
          4- Şifre değiştir
          5- Hesap silme""")

while True:
    printmenu()
    secim = input("İşlem Seçiniz: ")

    if secim == "1":
        username = input("Kullanıcı adınızı giriniz: ")
        password = input("Şifrenizi giriniz: ")
        user = search_username(username)
        if user == None or user[4] != password:
            print("Hatalı Kullanıcı adı veya Şifre")
        else:
            print("Giriş başarılı!")

    elif secim == "2":
        name = input("İsminizi Giriniz: ")
        lastname = input("Soyadınızı Girininiz: ")
        username = input("Kullanıcı adınızı giriniz: ")
        password = input("Şifrenizi Giriniz: ")
        user = search_username(username)
        if user != None:
            print("Bu kullanıcı adı daha önce alınmış")
        else:
            insert(name, lastname, username, password)
            print("Kayıt başarılı!")

    elif secim == "3":
        print("Program Sonlandırıldı")
        break

    elif secim == "4":
        print("Şifre sıfırlamaya hoş geldiniz")
        username = input("Kullanıcı adınızı giriniz: ")
        password = input("Şifrenizi giriniz: ")
        user = search_username(username)


        if user == None or user[4] != password:
                print("Hatalı Kullanıcı adı veya Şifre")
                continue

        else:
               new_password = input("Yeni şifrenizi giriniz: ")
        cursor.execute("""UPDATE USERS SET password = ? WHERE username = ?""", (new_password, username))
        print("Şifreniz başarıyla değiştirildi")


        conn.commit()


    elif secim == "5":

        username = input("Kullanıcı adınızı giriniz: ")
        password = input("şifrenizi Giriniz: ")
        user = search_username(username)
        if user == None or user[4] != password:
            print("Hatalı Kullanıcı adı veya Şifre")
        else:
            print("Profil başarıyla silindi ")

        delete_user(username)
        continue

conn.close()
