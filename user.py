from modulUser import*
import os

def user():
    while True:
        os.system('cls')
        print("#=================================#")
        print("||          LAMAN USER           ||")
        print("#=================================#")
        print("|| 1. Input Data Parkir          ||")
        print("|| 2. Keluar                     ||")
        print("#=================================#")

        pilihan = input("Silahkan pilih satu pilihan: ")

        if pilihan == '1':
            plat_nomor = get_plat_nomor()
            durasi_parkir = get_durasi_parkir()
            jenis_kendaraan = get_jenis_kendaraan()
            biaya_parkir = get_biaya_parkir(jenis_kendaraan, durasi_parkir)

            struk = tamp_struk_parkir(jenis_kendaraan, plat_nomor, durasi_parkir, biaya_parkir)
            if struk:
                simpan_struk(struk)
        
        elif pilihan == '2':
            print("Keluar dari sistem parkir.")
            break

        else:
            print("Input tidak valid. Pilih 1 atau 2.")
