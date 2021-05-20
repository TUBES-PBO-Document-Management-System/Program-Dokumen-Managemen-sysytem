import mysql.connector
import os
from time import sleep

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_dokumen"
)
class managemen_dokumen :
    
    def __init__(self):
        self.nama = str()
        self.ID_Kategori = int()
        self.ID_Topik = int()
        self.ID_Dokumen = int()
        self.tag = str()
    
    def input (self,kategori,topik,tag,nama):
        self.nama = nama
        self.ID_Kategori = kategori
        self.ID_Topik = topik
        self.tag = tag
        self.ID_Dokumen = 1
        mantopik = managemen_topik()
        mangori = managemen_kategori()
        
        if mangori.cekprimary(self.ID_Kategori) or mantopik.cekprimary(self.ID_Topik) : 
            self.insert()
        elif not mangori.cekprimary(self.ID_Kategori) :
            print("Tidak ada Kategori")
        else :
            print(" Tema Topik Tidak ada ")
    
    def deleteAll (self) :
        cursor = db.cursor()
        sql = "Delete from dokumen "
        cursor.execute(sql)
        db.commit()
        print("{} data berhasil dihapus".format(cursor.rowcount))

    def delete (self, ID) :
        cursor = db.cursor()
        sql = "Delete from dokumen where ID_Dokumen = %s " % (ID)
        cursor.execute(sql)
        db.commit()
        print("{} data berhasil dihapus".format(cursor.rowcount))

    def update (self, ID) :
        namabaru = str(input("Masukan Nama Baru : "))
        cursor = db.cursor()
        sql = "Update dokumen set Nama_File = '%s' where ID_Dokumen = %s " % (namabaru, ID)
        cursor.execute(sql)
        db.commit()
        print("{} data berhasil di Update".format(cursor.rowcount))

    def show (self) :
        cursor = db.cursor()
        sql = "select ID_Dokumen,kategori.Nama,tema.Tema,Folder_Penyimpanan,Tag,Nama_File from (dokumen natural join tema) join kategori where dokumen.ID_Kategori = kategori.ID_Kategori  "
        cursor.execute(sql)
        results = cursor.fetchall()

        if cursor.rowcount <= 0:
            print("Tidak ada data")
        else:
            print("ID_Dokumen\tKategori\tTopik\t\tDirektori\tTag\t\tNama File")
            for i in range(len(results)):
                for j in range(len(results[0])) :
                    print(results[i][j],end = "\t")
                    if j != len(results[0])-3 :
                        print(end = "\t")
                print()

    def insert(self) :
        while self.cekprimary() :
            self.ID_Dokumen += 1
        cursor = db.cursor()
        sql = "INSERT INTO dokumen (ID_Kategori, ID_Topik, ID_Dokumen, Tag, Nama_File) VALUES (%s, %s, %s, %s, %s)"
        val = (self.ID_Kategori, self.ID_Topik, self.ID_Dokumen, self.tag, self.nama)
        cursor.execute(sql, val)
        db.commit()
        print("{} data berhasil disimpan".format(cursor.rowcount))

    def cekprimary(self):
        cursor = db.cursor()
        sql = """select * from dokumen where ID_Dokumen = (%s) """   % (self.ID_Dokumen)
        cursor.execute(sql)
        row=cursor.fetchone()
        if row!=None:
            return True
        else :
            return False

class managemen_kategori :
    def __init__(self) :
        self.nama = str()
        self.ID_Kategori = int()

    def input (self, nama) :
        self.nama = nama
        self.ID_Kategori = 1
        self.insert()
    
    def deleteAll (self) :
        cursor = db.cursor()
        sql = "Delete from kategori "
        cursor.execute(sql)
        db.commit()
        print("{} data berhasil dihapus".format(cursor.rowcount))

    def delete (self, ID) :
        cursor = db.cursor()
        sql = "Delete from kategori where ID_Kategori = %s " % (ID)
        cursor.execute(sql)
        db.commit()
        print("{} data berhasil dihapus".format(cursor.rowcount))

    def update (self, ID) :
        namabaru = str(input("Masukan Nama Baru : "))
        cursor = db.cursor()
        sql = "Update kategori set Nama = '%s' where ID_Kategori = %s " % (namabaru, ID)
        cursor.execute(sql)
        db.commit()
        print("{} data berhasil di Update".format(cursor.rowcount))

    def show (self) :
        cursor = db.cursor()
        sql = "select * from kategori"
        cursor.execute(sql)
        results = cursor.fetchall()
        if cursor.rowcount < 0:
            print("Tidak ada data")
        else:
            for data in results:
                print(data)

    def insert(self) :
        while self.cekprimary(self.ID_Kategori) :
            self.ID_Kategori += 1
        cursor = db.cursor()
        sql = "INSERT INTO kategori (ID_Kategori,Nama) VALUES (%s, %s)"
        val = (self.ID_Kategori, self.nama)
        cursor.execute(sql, val)
        db.commit()
        print("{} data berhasil disimpan".format(cursor.rowcount))

    def cekprimary(self, ID):
        cursor = db.cursor()
        sql = """select * from kategori where ID_Kategori = (%s) """   % (ID)
        cursor.execute(sql)
        row=cursor.fetchone()
        if row!=None:
            return True
        else :
            return False
    
class managemen_topik :    
    def __init__(self) :
        self.tema = str()
        self.Folder_Penyimpanan = str()
        self.ID_Topik = int()

    def input (self, tema, Folder_Penyimpanan) :
        self.tema = tema
        self. Folder_Penyimpanan = Folder_Penyimpanan
        self.ID_Topik = 1
        self.insert()

    def deleteAll (self) :
        cursor = db.cursor()
        sql = "Delete from tema "
        cursor.execute(sql)
        db.commit()
        print("{} data berhasil dihapus".format(cursor.rowcount))

    def delete (self, ID) :
        cursor = db.cursor()
        sql = "Delete from tema where ID_Topik = %s " % (ID)
        cursor.execute(sql)
        db.commit()
        print("{} data berhasil dihapus".format(cursor.rowcount))

    def update (self, ID, conteks) :
        namabaru = str(input("Masukan Nama Baru : "))
        cursor = db.cursor()
        sql = "Update tema set %s = '%s' where ID_Topik = %s " % (conteks, namabaru, ID)
        cursor.execute(sql)
        db.commit()
        print("{} data berhasil di Update".format(cursor.rowcount))

    def show (self) :
        cursor = db.cursor()
        sql = "select * from tema"
        cursor.execute(sql)
        results = cursor.fetchall()
        if cursor.rowcount < 0:
            print("Tidak ada data")
        else:
            for data in results:
                print(data)

    def insert(self) :
        while self.cekprimary(self.ID_Topik) :
            self.ID_Topik += 1
        cursor = db.cursor()
        sql = "INSERT INTO tema (ID_Topik,Tema,Folder_Penyimpanan) VALUES (%s, %s, %s)"
        val = (self.ID_Topik, self.tema, self.Folder_Penyimpanan)
        cursor.execute(sql, val)
        db.commit()
        print("{} data berhasil disimpan".format(cursor.rowcount))

    def cekprimary(self, ID):
        cursor = db.cursor()
        sql = """select * from tema where ID_Topik = (%s) """   % (ID)
        cursor.execute(sql)
        row=cursor.fetchone()
        if row!=None:
            return True
        else :
            return False

def menu() :
    print("Selamat Datang Di Dokumen Managemen System")
    dokumen = managemen_dokumen()
    kategori = managemen_kategori()
    topik = managemen_topik()
    pilihan = 1
    while pilihan <= 3 :
        print("Silakan Anda Pilih Menu Yang Anda Inginkan")
        print("1. Dokumen ")
        print("2. Topik ")
        print("3. Kategori")
        pilihan=int(input("Silakan Masukan Pilihan Anda : "))
        os.system('cls')
        
        if pilihan == 1 :
            pilihan1 = 0
            while pilihan1 <= 5 :
                print("1. Menampilkan Seluruh Dokumen")
                print("2. Menambahkan Dokumen Baru")
                print("3. Mengedit Dokumen Yang Sudah Ada")
                print("4. Menghapus dokumen Yang Dipilih")
                print("5. Menghapus Seluruh Dokumen")
                print("6. Kembali Ke Menu")
                pilihan1=int(input("Silakan Masukan Pilihan Anda : "))
                if pilihan1 == 1 :
                    dokumen.show()
                elif pilihan1 == 2 :
                    dokumen.input(int(input("Masukan ID_Kategori : " )), int(input("Masukan ID_Topik : ")), str(input("Masukukan Tag :")), str(input("Masukan Nama Dokumen : "))) 
                elif pilihan1 == 3 :
                    dokumen.update(int(input("Masukan ID yang ingin di uodate : ")))
                elif pilihan1 == 4 :
                    dokumen.delete(int(input("Masukan ID data yang ingin dihapus : ")))
                elif pilihan1 == 5 :
                    dokumen.deleteAll()
                sleep(3)
                os.system('cls')

        elif pilihan == 2 :
            pilihan2 = 0
            while pilihan2 <= 5 :
                print("1. Menampilkan Seluruh Topik")
                print("2. Menambahkan Topik Baru")
                print("3. Mengedit Topik Yang Sudah Ada")
                print("4. Menghapus Topik Yang Dipilih")
                print("5. Menghapus Seluruh Topik")
                print("7. Kembali Ke Menu")
                pilihan2=int(input("Silakan Masukan Pilihan Anda : "))
                if pilihan2 == 1 :
                    topik.show()
                elif pilihan2 == 2 :
                    topik.input(str(input("Masukan Tema : ")),str(input("Masukan Lokasi Folder Penyimpanan : ")))
                elif pilihan2 == 3 :
                    print("1. Mengganti Topik\n2. Mengganti Folder Penyimpanan")
                    pilihanupdate = int(input("Masukan Pilahan Mu : "))
                    if pilihanupdate == 1 : 
                        topik.update(int(input("Masukan ID yang ingin di update : ")), "Tema")
                    elif pilihanupdate == 2 :
                        topik.update(int(input("Masukan ID yang ingin di update : ")), "Folder_Penyimpanan")
                elif pilihan2 == 4 :
                    topik.delete(int(input("Masukan ID data yang ingin dihapus : ")))
                elif pilihan2 == 5 :
                    topik.deleteAll()
                sleep(3)
                os.system('cls')

        elif pilihan == 3 :
            pilihan3 = 0
            while pilihan3 <= 5 :
                print("1. Menampilkan Seluruh Kategori")
                print("2. Menambahkan Kategori Baru")
                print("3. Mengedit Kategori Yang Sudah Ada")
                print("4. Menghapus Kategori Yang Dipilih")
                print("5. Menghapus Seluruh kategori")
                print("7. Kembali Ke Menu")
                pilihan3=int(input("Silakan Masukan Pilihan Anda : "))
                if pilihan3 == 1 :
                    kategori.show()
                elif pilihan3 == 2 :
                    kategori.input(str(input("Masukan Nama Kategori : ")))
                elif pilihan3 == 3 :
                    kategori.update(int(input("Masukan ID yang ingin di uodate : ")))
                elif pilihan3 == 4 :
                    kategori.delete(int(input("Masukan ID data yang ingin dihapus : ")))
                elif pilihan3 == 5 :
                    kategori.deleteAll()
                sleep(3)
                os.system('cls')   
        else :
            print("Jawaban Anda Tidak Sesuai, Anda akan kembali ke menu.")

menu()
