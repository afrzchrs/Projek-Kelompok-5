from admin import*
from user import*
import os
import sys

def main():
    lagi=False
    while not lagi:
        while True:
            try:
                os.system('cls')
                print("Selamat datang di aplikasi Parkir Politeknnik Negeri Bandung")
                print("\nLog in sebagai\n1.Admin\n2.User\n3.Keluar")
                pilihan=int(input("Masukkan pilihan(1/2/3):"))
                if pilihan == 1:
                    admin()
                elif pilihan == 2:
                    user()
                elif pilihan == 3:
                    lagi = True
                    sys.exit("Keluar paksa dari program")
                else:
                    print("Pilihan tidak valid, pilih 1 untuk Ya atau 2 untuk Tidak.")  # Menangani input selain 1 atau 2
            except ValueError:
                print("Input tidak valid! Harap masukkan angka 1 atau 2.")  # Menangani input selain angka
        
