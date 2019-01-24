import sqlite3
from sqlite3 import Error

def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    
    # hata çıkarsa boş gelsin.
    return None

def create_table(conn, sql_tablo):
    try:
        c = conn.cursor()
        c.execute(sql_tablo)
    except Error as e:
        print(e) 

def insert_musteri(conn, musteri):
    sql = """
          INSERT INTO Musteriler (TcNo, Ad, Soyad, DogumYili, Cinsiyet, Adres, Sehir)
          VALUES (?,?,?,?,?,?,?);
          """
    try:
        cur = conn.cursor()
        cur.execute(sql, musteri)
        return cur.lastrowid
    except Error as e:
        print(e)

def insert_hesap(conn, hesap):
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

def insert_transfer(conn, transfer):
    sql = """
          INSERT INTO Transferler (TcNo, HesapNo, Tutar)
            VALUES (?,?,?);
          """
    try:
        cur = conn.cursor()
        cur.execute(sql, transfer)
        return cur.lastrowid
    except Error as e:
        print(e)

def insert_odeme(conn, odeme):
    sql = """
          INSERT INTO Ödemeler (TcNo, HesapNo, OdemeTuru)
            VALUES (?,?,?);
          """
    try:
        cur = conn.cursor()
        cur.execute(sql, odeme )
        return cur.lastrowid
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

def select_musteri_byTcNo(self, conn, TcNo):
    sql = """SELECT * FROM Musteriler WHERE TcNo = ? ;"""
    try:
        cur = conn.cursor()
        cur.execute(sql, TcNo)
        musteri = cur.fetchone()
        return musteri 
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

def select_transfer(self, conn):
    sql = """SELECT * FROM Transferler;"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        transferler = cur.fetchall()
        return transferler
    except Error as e:
        print(e)

def select_odeme(self, conn):
    sql = """SELECT * FROM Ödemeler;"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        ödemeler = cur.fetchall()
        return ödemeler
    except Error as e:
        print(e)


database = 'banka.db'
conn = create_connection(database)
sql_musteri_tablo = """
                  CREATE TABLE IF NOT EXISTS Musteriler(
                  TcNo INTEGER NOT NULL ,
                  Ad TEXT NOT NULL,
                  Soyad TEXT NOT NULL,
                  DogumYili INTEGER NOT NULL,
                  Cinsiyet TEXT NOT NULL,
                  Adres TEXT NOT NULL ,
                  Sehir TEXT NOT NULL
                  );
                  """


sql_hesap_tablo = """
                  CREATE TABLE IF NOT EXISTS Hesaplar(
                  HesapNo INTEGER PRIMARY KEY
                  );
                  """

sql_transfer_tablo = """
                  CREATE TABLE IF NOT EXISTS Transferler(
                  TNo INTEGER PRIMARY KEY
                     );
                    """

sql_odeme_tablo = """
                  CREATE TABLE IF NOT EXISTS Odemeler(
                  ONo INTEGER PRIMARY KEY
                     );
                    """


if conn is not None:
    with conn:
        
        create_table(conn, sql_musteri_tablo)
        create_table(conn, sql_hesap_tablo)
        create_table(conn, sql_transfer_tablo)
        create_table(conn, sql_odeme_tablo)

        #mus1= (1,"Rahime","Yılmaz",1994,"Kadın","Tekno","ANKARA")
        #insert_musteri(conn,mus1)