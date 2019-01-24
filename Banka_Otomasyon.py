import sys
import sqlite3
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QPushButton, 
                            QLabel, QHBoxLayout, QGridLayout, QAction, QTabWidget,
                            QVBoxLayout, QTableWidget, QTableWidgetItem, QDialog,
                            QLineEdit, QMessageBox,QStatusBar)
from PyQt5.QtGui import QIcon,QColor,QPixmap
from PyQt5.QtCore import Qt,QSize

from banka import BankaDbIslem

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.creat_connect()
        self.init_ui()

    def creat_connect(self):
        connect = sqlite3.connect("giris.db")

        self.cursor = connect.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS bilgiler(kullanıcı_adı TEXT ,parola TEXT)")
        connect.commit()

    def init_ui(self):

        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş")
        self.kaydol = QtWidgets.QPushButton("Kaydol")
        self.yazi_alani =QtWidgets.QLabel("")
        self.user =QtWidgets.QLabel("User   :")
        self.password = QtWidgets.QLabel("Parola :")
        self.hatirlat = QtWidgets.QCheckBox("Hatırla")
        self.unuttum = QtWidgets.QPushButton("Şifremi unuttum")



        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.user)
        h_box1.addWidget(self.kullanici_adi)
        h_box1.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.password)
        h_box2.addWidget(self.parola)
        #h_box2.addWidget(self.hatirlat)
        h_box2.addStretch()



        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.yazi_alani)
        h_box3.addStretch()

        h_box5 = QtWidgets.QHBoxLayout()
        h_box5.addStretch()
        h_box5.addWidget(self.hatirlat)
        h_box5.addWidget(self.unuttum)
        h_box5.addStretch()



        h_box4 = QtWidgets.QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.giris)
        h_box4.addWidget(self.kaydol)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)

        v_box.addLayout(h_box3)
        v_box.addLayout(h_box5)
        v_box.addStretch()
        v_box.addLayout(h_box4)


        self.user.setFixedSize(35,20)
        self.password.setFixedSize(35,20)
        self.kullanici_adi.setFixedSize(120,20)
        self.parola.setFixedSize(120,20)


        self.setLayout(v_box)

        self.giris.clicked.connect(self.login)
        self.kaydol.clicked.connect(self.kaydoll)
        self.unuttum.clicked.connect(self.yenile)





        self.setStyleSheet("background-color:grey;")
        self.setGeometry(400,100,300,300)
        self.setFixedSize(300,300)
        self.setWindowTitle("GİRİŞ SİSTEMİ")
        #self.giris.setStyleSheet("background-color")
        #self.yazi_alani.setStyleSheet("background-color: red")
        #self.kullanici_adi.setStyleSheet("background-color: red")
        self.show()

    def login(self):

        ad  = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("SELECT * FROM bilgiler WHERE kullanıcı_adı= ? and parola = ?",(ad,par))

        data = self.cursor.fetchall()

        if len(data)==0:
            self.yazi_alani.setText("Yanlış giriş")

        else:
            pencere2.show()
            self.yazi_alani.setText("hoş geldiniz")

    def kaydoll(self):

        pencere3.show()

    def yenile(self):
        pencere4.show()

class Pencere2(QtWidgets.QWidget):

    def initUI(self):
        styleSheet = """
    QPushButton {
    background: grey;
    border-radius:5px;
    border:1px solid #18ab29;
    color:#ffffff;
    font-family:arial;
    font-size:15px;
    font-weight:bold;
    text-decoration:none;
    padding-right:10px;
    outline: 0;
}
QPushButton#Button {
    background: lightseagreen;
    border-radius:5px;
    border:1px solid #18ab29;
    color:#ffffff;
    font-family:arial;
    font-size:15px;
    font-weight:bold;
    text-decoration:none;
    padding-right:10px;
    outline: 0;
}
                    """
        self.setStyleSheet(styleSheet) 
        self.setGeometry(0, 0, 800, 600)
        self.setStyleSheet("background-color:grey")
        self.setWindowTitle("Banka Takip Programı")
        self.setWindowIcon(QIcon('favicon.png'))


    def __init__(self):
        super().__init__()
        self.initUI()


        self.layout = QVBoxLayout(self)
        self.tab = QTabWidget()
        self.secilen = None
        #musteri tab
        self.musteri = QWidget()
        self.tab.addTab(self.musteri, "Müşteriler")

        self.musteri.grid = QGridLayout()
        self.mus_btn_listele = QPushButton("Listele")
        self.mus_btn_listele.setObjectName("Button")
        self.mus_btn_listele.setFixedSize(250,250)
        self.mus_btn_listele.clicked.connect(self.musteri_listele)
        self.mus_btn_ekle = QPushButton("Ekle")
        self.mus_btn_ekle.setFixedSize(250,250)
        self.mus_btn_ekle.clicked.connect(self.musteri_ekle)
        self.mus_btn_guncel = QPushButton("Güncelle")
        self.mus_btn_guncel.setFixedSize(250,250)
        self.mus_btn_guncel.clicked.connect(self.musteri_guncelle)
        self.mus_btn_sil = QPushButton("Sil")
        self.mus_btn_sil.setFixedSize(250,250) 
        self.mus_btn_sil.clicked.connect(self.musteri_sil)

        self.musteri.grid.addWidget(self.mus_btn_listele, 0, 0)
        self.musteri.grid.addWidget(self.mus_btn_ekle, 0, 1)
        self.musteri.grid.addWidget(self.mus_btn_guncel, 0, 2)
        self.musteri.grid.addWidget(self.mus_btn_sil, 0, 3)
        self.musteri.setLayout(self.musteri.grid) 

        self.layout.addWidget(self.tab)
        self.setLayout(self.layout)


        #hesap tab
        self.hesap = QWidget()
        self.tab.addTab(self.hesap, "Hesaplar")

        self.hesap.grid = QGridLayout()
        self.hesap.setLayout(self.hesap.grid)
           
        self.layout.addWidget(self.tab)
        self.setLayout(self.layout)

        #transferler tab
        self.transfer = QWidget()
        self.tab.addTab(self.transfer, "Transferler")

        self.transfer.grid = QGridLayout()
        self.transfer.setLayout(self.transfer.grid)
           
        self.layout.addWidget(self.tab)
        self.setLayout(self.layout)


        #ödemeler tab
        self.ödeme = QWidget()
        self.tab.addTab(self.ödeme, "Ödemeler")

        self.ödeme.grid = QGridLayout()
        self.ödeme.setLayout(self.ödeme.grid)
           
        self.layout.addWidget(self.tab)
        self.setLayout(self.layout)

#Müşteri Fonksiyonları
    def musteri_ekle(self):
        diyalog = MusteriEkleDiyalog(self)
        diyalog.setGeometry(100, 100, 700, 300)
        diyalog.show()

    def musteri_listele(self):
        bandb = BankaDbIslem('banka.db')
        conn = bandb.create_connection()
        self.mus_btn_listele.hide()
        self.mus_btn_ekle.hide()
        self.mus_btn_guncel.hide()
        self.mus_btn_sil.hide()

        if conn is not None:
            with conn:
                musteri_liste = bandb.select_musteri(conn)
                self.musteri_table = QTableWidget()

                self.btn_guncelle= QPushButton('Güncelle')
                self.btn_guncelle.setObjectName("Button")
                self.geri_buton= QPushButton()
                
                self.geri_buton.setObjectName("Button")
                
                self.geri_buton.setIcon(QIcon('geri.png'))
                
                self.btn_sil= QPushButton('Sil')
                self.btn_sil.setObjectName("Button")
                self.musteri.grid.addWidget(self.geri_buton,2,1)
                self.musteri_table.setRowCount(len(musteri_liste))
                self.musteri_table.setColumnCount(len(musteri_liste[0]))
                self.musteri_table.setHorizontalHeaderLabels(['TcNo','Ad','Soyad','Doğum Yılı','Cinsiyet','Adres','Sehir'])
                self.musteri.grid.addWidget(self.musteri_table,0,1) 
                self.musteri_table.cellClicked.connect(self.hucre_secildi)

                for i in range(len(musteri_liste)):
                    for j in range(len(musteri_liste[0])):
                        self.musteri_table.setItem(i, j, QTableWidgetItem(str(musteri_liste[i][j])))
                self.geri_buton.clicked.connect(self.geri)
        
    def hucre_secildi(self, row, column):
        item = self.musteri_table.item(row, 0)
        self.secilen = int(item.text())

    def musteri_guncelle(self, musteri):
        self.musteri_listele()
        self.musteri.grid.addWidget(self.btn_guncelle,1,1)
        self.btn_guncelle.show()
        self.btn_guncelle.clicked.connect(self.diyalog_ekrani)
        self.geri_buton.clicked.connect(self.geri)

    def diyalog_ekrani(self):
        diyalog = MusteriGuncelleDiyalog (self.secilen, self)
        diyalog.setGeometry(100, 100, 400, 300)
        diyalog.show()

    def hucre_secildi(self, row, column):
        item = self.musteri_table.item(row, 0)
        self.secilen = int(item.text())

    def sil(self):
        bandb = BankaDbIslem('banka.db')
        conn = bandb.create_connection()
        if conn is not None:
            with conn :
                etkilenen_kayit = bandb.delete_musteri(conn, (self.secilen,))
                print(etkilenen_kayit)
                while(self.musteri_table.rowCount() > 0):
                    self.musteri_table.removeRow(0)
                
                musteri_liste = bandb.select_musteri(conn)
                self.musteri_table.setRowCount(len(musteri_liste))
                self.musteri_table.setColumnCount(len(musteri_liste[0]))
                for i in range(len(musteri_liste)):
                    for j in range(len(musteri_liste[0])):
                        self.musteri_table.setItem(i, j, QTableWidgetItem(str(musteri_liste[i][j])))
                self.musteri_table.show()

    def geri(self):
        self.btn_sil.hide()
        self.musteri_table.hide()
        self.geri_buton.hide()
        self.btn_guncelle.hide()
        self.mus_btn_listele.show()
        self.mus_btn_ekle.show()
        self.mus_btn_guncel.show()
        self.mus_btn_sil.show()

    def musteri_sil(self):
        self.musteri_listele()
        self.musteri.grid.addWidget(self.btn_sil,1,1)
        self.btn_sil.show()
        self.btn_sil.clicked.connect(self.sil)
        self.geri_buton.clicked.connect(self.geri)

class Pencere3(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.gorsel()
        self.connect()

    def connect(self):

        self.connec = sqlite3.connect("kayitlar.db")
        self.im =self.connec.cursor()

        self.im.execute("CREATE TABLE IF NOT EXISTS kayit(ad TEXT,soyad TEXT,sifre TEXT,email TEXT)")


    def gorsel(self):
        self.ad = QtWidgets.QLabel("    Ad :")
        self.soyad = QtWidgets.QLabel("Soyad :")
        self.adi = QtWidgets.QLineEdit()
        self.soyadi= QtWidgets.QLineEdit()
        self.email = QtWidgets.QLabel("  Email :")
        self.emaili =QtWidgets.QLineEdit()
        self.passwor =QtWidgets.QLabel("  Şifre :")
        self.passworu = QtWidgets.QLineEdit()
        self.kaydet = QtWidgets.QPushButton("Kaydet")

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.ad)
        h_box1.addWidget(self.adi)
        h_box1.addStretch()

        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.soyad)
        h_box2.addWidget(self.soyadi)
        h_box2.addStretch()

        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.email)
        h_box3.addWidget(self.emaili)
        h_box3.addStretch()

        h_box5 = QtWidgets.QHBoxLayout()
        h_box5.addStretch()
        h_box5.addWidget(self.passwor)
        h_box5.addWidget(self.passworu)
        h_box5.addStretch()

        h_box4 = QtWidgets.QHBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.kaydet)
 
        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box5)
        v_box.addLayout(h_box4)

        self.setLayout(v_box)


        self.ad.setFixedSize(35,20)
        self.adi.setFixedSize(120,20)
        self.soyad.setFixedSize(35,20)
        self.soyadi.setFixedSize(120,20)
        self.email.setFixedSize(35,20)
        self.emaili.setFixedSize(120,20)
        self.passwor.setFixedSize(35,20)
        self.passworu.setFixedSize(120,20)



        self.setWindowTitle("           KAYDOL 2             ")
        self.setStyleSheet("background-color:grey")
        self.setFixedSize(300, 300)

        self.kaydet.clicked.connect(self.account)

    def account(self):
        ad = self.adi.text()
        soyad = self.soyadi.text()
        email= self.emaili.text()
        sifre = self.passworu.text()

        self.im.execute("INSERT INTO kayit VALUES(?,?,?,?)",(ad,soyad,sifre,email))
        self.connec.commit()

class Pencere4(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.gorsel()

    def gorsel(self):
        self.email_lable = QtWidgets.QLabel("Email :")
        self.email_line =QtWidgets.QLineEdit()
        self.gonder = QtWidgets.QPushButton("Gönder")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.email_lable)
        h_box.addWidget(self.email_line)
        h_box.addStretch()

        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box.addWidget(self.gonder)
        h_box1.addStretch()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box1)
        v_box.addStretch()

        self.setLayout(v_box)
        self.setWindowTitle("ŞİFRE YENİLEME")
        self.setStyleSheet("background-color :grey")
        self.setFixedSize(250,100)

class MusteriEkleDiyalog(QDialog):
    def __init__(self,  parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Musteri Ekle")
        self.layout = QGridLayout()
        
        self.lbl_tc = QLabel('Tc No :')
        self.le_tc = QLineEdit()

        self.lbl_ad = QLabel('Ad :')
        self.le_ad = QLineEdit()

        self.lbl_soyad = QLabel('Soyad :')
        self.le_soyad = QLineEdit()
        
        
        self.lbl_dy = QLabel('Doğum Yılı :')
        self.le_dy = QLineEdit()
        
        self.lbl_cins = QLabel('Cinsiyet :')
        self.le_cins = QLineEdit()

        self.lbl_adres = QLabel('Adres :')
        self.le_adres = QLineEdit()
        
        self.lbl_il = QLabel('Şehir :')
        self.le_il = QLineEdit()

        self.btn_ekle = QPushButton('Ekle ')
        self.btn_ekle.setObjectName("Button")
        self.btn_ekle.clicked.connect(self.musteri_ekle)


        self.layout.addWidget(self.lbl_tc, 0, 0)
        self.layout.addWidget(self.le_tc, 0, 1)
        self.layout.addWidget(self.lbl_ad, 1, 0)
        self.layout.addWidget(self.le_ad, 1, 1)
        self.layout.addWidget(self.lbl_soyad, 2, 0)
        self.layout.addWidget(self.le_soyad, 2, 1)
        self.layout.addWidget(self.lbl_dy, 3, 0)
        self.layout.addWidget(self.le_dy, 3, 1)
        self.layout.addWidget(self.lbl_cins, 4, 0)
        self.layout.addWidget(self.le_cins, 4, 1)
        self.layout.addWidget(self.lbl_adres, 5, 0)
        self.layout.addWidget(self.le_adres, 5, 1)
        self.layout.addWidget(self.lbl_il, 6, 0)
        self.layout.addWidget(self.le_il, 6, 1)
        self.layout.addWidget(self.btn_ekle, 7, 0, 2, 0)
        self.setLayout(self.layout)
    
    def musteri_ekle(self):
        bandb = BankaDbIslem('banka.db')
        conn = bandb.create_connection()
        musteri = (int(self.le_tc.text()), self.le_ad.text(), self.le_soyad.text(),
              int(self.le_dy.text()), self.le_cins.text(), self.le_adres.text(),self.le_il.text())
        if conn is not None:
            with conn: 
                etkilenen_kayit = bandb.insert_musteri(conn,musteri)
                msg = QMessageBox()
                msg.setWindowTitle('Uyarı')
                msg.setIcon(QMessageBox.Information)
                msg.setText("kayıt eklendi.")
                donen = msg.exec_()
                if donen == 1024:
                    self.le_tc.setText('')
                    self.le_ad.setText('')
                    self.le_soyad.setText('')
                    self.le_dy.setText('')
                    self.le_cins.setText('')
                    self.le_adres.setText('')
                    self.le_il.setText('')

class MusteriGuncelleDiyalog(QDialog):

    def __init__(self, secilen, parent=None):
        super().__init__(parent)
        mst = self.musteri_getir(secilen)
        self.setWindowTitle("Müşteri Güncelle")
        self.layout = QGridLayout()

        self.lbl_tckn = QLabel('Tc No :')
        self.le_tckn = QLineEdit()
        self.le_tckn.setText(str(mst[0]))

        self.lbl_ad = QLabel('Ad :')
        self.le_ad = QLineEdit()
        self.le_ad.setText(str(mst[1]))

        self.lbl_soyad = QLabel('Soyad :')
        self.le_soyad = QLineEdit()
        self.le_soyad.setText(str(mst[2]))

        self.lbl_dy = QLabel('Doğum Yılı :')
        self.le_dy = QLineEdit()
        self.le_dy.setText(str(mst[3]))

        self.lbl_cins = QLabel('Cinsiyet :')
        self.le_cins = QLineEdit()
        self.le_cins.setText(str(mst[4]))

        self.lbl_adres = QLabel('Adres :')
        self.le_adres = QLineEdit()
        self.le_adres.setText(str(mst[5]))

        self.lbl_il = QLabel('Şehir :')
        self.le_il = QLineEdit()
        self.le_il.setText(str(mst[6]))

        self.btn_guncel= QPushButton('Güncelle')
        self.btn_guncel.setObjectName("Button")
        self.btn_guncel.clicked.connect(self.musteri_guncel)

        self.layout.addWidget(self.lbl_tckn, 0, 0)
        self.layout.addWidget(self.le_tckn, 0, 1)
        self.layout.addWidget(self.lbl_ad, 1, 0)
        self.layout.addWidget(self.le_ad, 1, 1)
        self.layout.addWidget(self.lbl_soyad, 2, 0)
        self.layout.addWidget(self.le_soyad, 2, 1)
        self.layout.addWidget(self.lbl_dy, 3, 0)
        self.layout.addWidget(self.le_dy, 3, 1)
        self.layout.addWidget(self.lbl_cins, 4, 0)
        self.layout.addWidget(self.le_cins, 4, 1)
        self.layout.addWidget(self.lbl_adres, 5, 0)
        self.layout.addWidget(self.le_adres, 5, 1)
        self.layout.addWidget(self.lbl_il, 6, 0)
        self.layout.addWidget(self.le_il, 6, 1)
        self.layout.addWidget(self.btn_guncel,7, 0, 2, 0)
        self.setLayout(self.layout)


    def musteri_guncel(self):
        bandb = BankaDbIslem('banka.db')
        conn = bandb.create_connection()

        musteri = (int(self.le_tckn.text()), self.le_ad.text(),self.le_soyad.text(), int(self.le_dy.text()), self.le_cins.text(), 
        self.le_adres.text(),self.le_il.text())
        if conn is not None:
            with conn:
                etkilenen_kayit = bandb.update_musteri(conn, musteri)  


    def musteri_getir(self, secilen):
        bandb = BankaDbIslem('banka.db')
        conn = bandb.create_connection()

        if conn is not None:
            with conn:
                mst = bandb.select_musteri_byTcNo(conn, (secilen,))
                return mst
        
if __name__ == '__main__':
 uygulama = QtWidgets.QApplication(sys.argv)

 pencere = Pencere()
 pencere2 = Pencere2()
 pencere3 = Pencere3()
 pencere4 = Pencere4()
 sys.exit(uygulama.exec_())
 