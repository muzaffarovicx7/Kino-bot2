from sqlite3 import connect, Error



def KinoOlish():
    try:
        c = connect('kino.db')
        cursor = c.cursor()
        cursor.execute("SELECT id, name FROM kino_uchun")
        kino = cursor.fetchall()
        return kino
    except (Error, Exception) as error:
        print("Xato: ", error)
    finally:
        if c:
            cursor.close()
            c.close()




def KinoDelete(id):
    try:
        c = connect('kino.db')
        cursor = c.cursor()
        cursor.execute("delete from KINO_UCHUN where ID = ?", (id,))
        c.commit()
        print("Kino o'chirildi.")
    except (Error, Exception) as error:
        print("Xato: ", error)
    finally:
        if c:
            cursor.close()
            c.close()





def Obunachilar():
    try:
        c = connect('kino.db')
        cursor = c.cursor()
        cursor.execute("select * from obunachi")
        kino = cursor.fetchall()
        return kino
    except (Error, Exception) as error:
        print("Xato: ", error)
    finally:
        if c:
            cursor.close()
            c.close()




def KinoRead(id): 
    try:
        c = connect('kino.db')
        cursor = c.cursor()
        cursor.execute("select * from KINO_UCHUN where ID = ?", (id,))
        kino = cursor.fetchone()
        return kino
    except (Error, Exception) as error:
        print("Xato: ", error)
    finally:
        if c:
            cursor.close()
            c.close()












def KinoAdd(name, disc, link):
    try:
        c = connect('kino.db')
        cursor = c.cursor()
        cursor.execute("insert into KINO_UCHUN(NAME, DESCRIPTION, LINK) values(?, ?, ?)", (name, disc, link))
        c.commit()
        print("Jadval yaratildi.")
    except (Error, Exception) as error:
        print("Xato: ", error)
    finally:
        if c:
            cursor.close()
            c.close()



def ObunachilarAdd(name, id):
    try:
        c = connect('kino.db')
        cursor = c.cursor()
        cursor.execute("insert into Obunachi(name, telegram_id) values(?, ?)", (name, id))
        c.commit()
        print("Jadval yaratildi.")
    except (Error, Exception) as error:
        print("Xato: ", error)
    finally:
        if c:
            cursor.close()
            c.close()







# try:
#     c = connect('kino.db')
#     cursor = c.cursor()
#     cursor.execute("""
#                     CREATE TABLE Obunachi(
#                     ID INTEGER PRIMARY KEY NOT NULL,
#                     NAME TEXT NOT NULL,
#                     TELEGRAM_ID INTEGER NOT NULL UNIQUE
#                     );
#                     """)
#     c.commit()
#     print("Jadval yaratildi.")
# except (Error, Exception) as error:
#     print("Xato: ", error)
# finally:
#     if c:
#         cursor.close()
#         c.close()









# try:
#     c = connect('kino.db')
#     cursor = c.cursor()
#     cursor.execute("""
#                     CREATE TABLE KINO_UCHUN(
#                     ID INTEGER PRIMARY KEY NOT NULL,
#                     NAME TEXT NOT NULL,
#                     DESCRIPTION TEXT NOT NULL,
#                     LINK TEXT NOT NULL
#                     );
#                     """)
#     c.commit()
#     print("Jadval yaratildi.")
# except (Error, Exception) as error:
#     print("Xato: ", error)
# finally:
#     if c:
#         cursor.close()
#         c.close()
    
