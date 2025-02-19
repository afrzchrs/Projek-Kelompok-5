from modulAdmin import*
import os

def admin():
    while True:
        os.system('cls')
        print("#=================================#")
        print("||          LAMAN ADMIN          ||")
        print("#=================================#")
        print("|| 1. Lihat Riwayat Parkir       ||")
        print("|| 2. Keluar                     ||")
        print("#=================================#")

        pilihan = input("Silahkan pilih satu pilihan: ")

        if pilihan == '1':
            riwayat()
        
        elif pilihan == '2':
            print("Keluar dari sistem parkir.")
            break

        else:
            print("Input tidak valid. Pilih 1 atau 2.")
