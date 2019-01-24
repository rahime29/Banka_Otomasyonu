import sqlite3
from sqlite3 import Error

class BankaDbIslem:
    def __init__(self, database):
        self.database = database
        
    def create_connection(self):
        """
        Veritabanına bağlanır.

        return conn: veritabanı bağlantısı döner.
        """
        try:
            conn = sqlite3.connect(self.database)
            return conn
        except Error as e:
            print(e)
        
        # hata çıkarsa boş gelsin.   
        return None

    def create_table(self, conn, sql_tablo):
        try:
            c = conn.cursor()
            c.execute(sql_tablo)
        except Error as e:
            print(e) 


    def insert_musteri(self, conn, musteri):
        sql = """
            INSERT INTO Musteriler(TcNo, Ad, Soyad, DogumYili, Cinsiyet, Adres, Sehir)
            VALUES (?,?,?,?,?,?,?);
            """
        try:
            cur = conn.cursor()
            cur.execute(sql, musteri)
            return cur.lastrowid
        except Error as e:
            print(e)
            
    def insert_hesap(self, conn, hesap):
        sql = """
            INSERT INTO Hesaplar (HesapNo)
            VALUES (?);
            """
        try:
            cur = conn.cursor()
            cur.execute(sql, hesap)
            return cur.lastrowid
        except Error as e:
            print(e)


    def insert_transfer(self, conn, transfer):
        sql = """
            INSERT INTO Transferler ()
            VALUES ();
            """
        try:
            cur = conn.cursor()
            cur.execute(sql, transfer)
            return cur.lastrowid
        except Error as e:
            print(e)

    def insert_odeme(self, conn, odeme):
        sql = """
            INSERT INTO Ödemeler ()
            VALUES ();
            """
        try:
            cur = conn.cursor()
            cur.execute(sql, odeme)
            return cur.lastrowid
        except Error as e:
            print(e)
            
    def select_hesap(self, conn):
        sql = """SELECT * FROM Hesaplar;"""
        try:
            cur = conn.cursor()
            cur.execute(sql)
            hesaplar = cur.fetchall()
            return hesaplar
        except Error as e:
            print(e)

    def select_hesap_byId(self, conn, id):
        sql = """SELECT * FROM Hesaplar WHERE HesapNo = ? ;"""
        try:
            cur = conn.cursor()
            cur.execute(sql, id)
            hesap = cur.fetchone()
            return hesap
        except Error as e:
            print(e)

    def select_musteri(self, conn):
        sql = """SELECT * FROM Musteriler;"""
        try:
            cur = conn.cursor()
            cur.execute(sql)
            musteriler = cur.fetchall()
            return musteriler
        except Error as e:
            print(e)


    def select_musteri_byTcNo(self, conn,id):
        sql = """SELECT * FROM Musteriler WHERE TcNo = ? ;"""
        try:
            cur = conn.cursor()
            cur.execute(sql,id)
            musteri = cur.fetchone()
            return musteri
        except Error as e:
            print(e)


    def update_musteri(self, conn, musteri):
        sql ="""UPDATE Musteriler SET Ad=?, Soyad=?, DogumYili=?, Cinsiyet=?, Adres=?, Sehir=? WHERE TcNo=?;"""
        try:
            cur = conn.cursor()
            cur.execute(sql, musteri)
            return cur.rowcount
        except Error as e:
            print(e)

    def delete_musteri(self, conn, id):
        sql ="""DELETE FROM Musteriler WHERE TcNo=?; """
        try:
            cur = conn.cursor()
            cur.execute(sql, id)
            return cur.rowcount
        except Error as e:
            print(e)
