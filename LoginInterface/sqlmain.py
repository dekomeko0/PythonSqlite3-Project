from Sqlite3 import *

conn = sql.connect('data.db')
cursor = conn.cursor()
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
          3- Programı Sonlandır""")

while True:
    printmenu()
    secim = input("İşlem Seçiniz: ")
    
    if secim == "1":
            cursor.execute("SELECT COUNT (*) FROM USERS")
            count = cursor.fetchone()[0]
            if count == 0:
                print("Herhangi bir kullanıcı yok")
                continue
            
            else:
                username = input("Kullanıcı adınızı giriniz: ")
                password = input("Şifrenizi giriniz: ")
                user = search_username(username)
                if user == None or user[4] != password:
                    print("Hatalı Kullanıcı adı veya Şifre")
                else:
                    print("Giriş başarılı!")

                    print("""Profil Seçenekleri:
                        1- Şifre Değiştir
                        2- Kullanıcı adı değiştir
                        3- Hesabı sil
                        4- Kayıtlı profiller""")
        
                    secim = input("İşlem Seçiniz: ")
        
                    if secim == "1":
                              print("Şifre sıfırlamaya hoş geldiniz")
                              password = input("Şifrenizi giriniz: ")
                              user = search_username(username)
                              if user[4] != password:
                                  print("hatalı şifre girdiniz")
                                  
                              else:
                                  new_password = input("Yeni şifrenizi giriniz: ")
                                  cursor.execute("""UPDATE USERS SET password = ? WHERE username = ?""", (new_password, username))
                                  print("Şifreniz başarıyla değiştirildi")
        
                    if secim == "2":
                    
                              print("Kullanıcı Adı Değiştiriyorsunuz")
                              user = search_username(username)
                              input("Şifrenizi giriniz: ")
                              if user[4] != password:
                                  print("Hatalı Şifre girdiniz")
        
                              else:
                                  new_username = input("Yeni Kullanıcı adınızı giriniz: ")
                                  cursor.execute("""UPDATE USERS SET username = ? WHERE username = ?""", (new_username, username))
                                  print("Kullanıcı Adınız başarıyla değiştirildi")
        
        
        
                    elif secim == "3":
                    
                          username = input("Kullanıcı adınızı giriniz: ")
                          password = input("şifrenizi Giriniz: ")
                          user = search_username(username)
                          if user == None or user[4] != password:
                              print("Hatalı Kullanıcı adı veya Şifre")
                          else:
                              print("Profil başarıyla silindi ")
        
                          delete_user(username)
                          continue   

                    else:
                        print("Hatalı Giriş")
                        continue    
                   #elif secim == "5":
                    
                    #      username = input("Kullanıcı adınızı giriniz")
                    #    conn.sql('data.db')
                    #      user = search_username(username)
                    #    conn.cursor()
                    #    if user == None:
                    #          print("Hatalı Kullanıcı adı")
                    #          continue
                    #        
                    #      else:
                    #          cursor.execute(""" """)/*
        
        
                    elif secim == "4":        
                    
                              password = input("Admin şifresi: ")
        
                              if password == "admin":
                                
                                  conn = sql.connect('data.db')  
                                  cursor = conn.cursor()
                                  cursor.execute( """SELECT * from USERS""")
                                  list_all = cursor.fetchall()
                                  for users in list_all:
                                      print(users)
                                  conn.commit()
                                  conn.close() 
                              else:
                                  print("Hatalı giriş")
                                  break   
    
    elif secim == "2":
        name = input("İsminizi Giriniz: ")
        lastname = input("Soyadınızı Girininiz: ")
        username = input("Kullanıcı adınızı giriniz: ")
        password = input("Şifrenizi Giriniz: ")
        if password =="" or username=="" or name=="" or lastname =="":
            print("Hatalı giriş")
            continue
        else:
            user = search_username(username)
            if user != None:
                print("Bu kullanıcı adı daha önce alınmış")
            else:
                insert(name, lastname, username, password)
                print("Kayıt başarılı!")

    elif secim == "3":
        print("Program Sonlandırıldı")
        break
    else: 
        print("Hatalı giriş")
        continue

conn.close()