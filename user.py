def get_jenis_kendaraan(durasi_parkir):
    jenis_kendaraan = input("Masukkan jenis kendaraan (a untuk Motor, b untuk Mobil): ")
    biaya = get_biaya_parkir(jenis_kendaraan, durasi_parkir)
    print(f"Biaya parkir untuk jenis kendaraan {jenis_kendaraan} selama {durasi_parkir} jam adalah {biaya}.")

def get_plat_nomor():
    plat_nomor = input("Masukkan plat nomor kendaraan: ")
    return plat_nomor

def get_durasi_parkir():
    durasi_parkir = int(input("Masukkan durasi parkir dalam jam: "))
    return durasi_parkir

def get_biaya_parkir(jenis_kendaraan, durasi_parkir):
    if jenis_kendaraan.lower() == 'a':  # Motor
        if durasi_parkir > 1:
            return 1000 + ((durasi_parkir - 1) * 1500)
        else:
            return 1000
    else:  # Mobil
        if durasi_parkir > 1:
            return 3000 + ((durasi_parkir - 1) * 3500)
        else:
            return 3000

while True:
    print("#=================================#")
    print("||          LAMAN USER           ||")
    print("#=================================#")
    print("|| 1. Plat Nomor Kendaraan       ||")
    print("|| 2. Durasi Parkir              ||")
    print("|| 3. Jenis Kendaraan            ||")
    print("#=================================#")
    
    pilihan = int(input("Silahkan Pilih satu pilihan :"))
    
    if pilihan == 1:
        plat_nomor = get_plat_nomor()
        print(f"Plat Nomor Kendaraan: {plat_nomor}")
        
    elif pilihan == 2:
        durasi_parkir = get_durasi_parkir()
        print(f"Durasi Parkir: {durasi_parkir} jam")
        
    elif pilihan == 3:
        durasi_parkir = get_durasi_parkir()  # Need to get durasi_parkir before checking jenis_kendaraan
        get_jenis_kendaraan(durasi_parkir)
    
    else:
        print("Input tidak valid")

    ulang = input("Apakah anda ingin mencoba lagi? (y/n): ")
    if ulang != "y":
        print("Keluar")
        break
