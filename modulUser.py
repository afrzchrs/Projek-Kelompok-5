def tamp_struk_parkir(jenis_kendaraan, plat_nomor, durasi_parkir, biaya_parkir):
    if jenis_kendaraan.lower() == 'a':
        jenis_kendaraan = "Motor"
    elif jenis_kendaraan.lower() == 'b':
        jenis_kendaraan = "Mobil"
    else:
        print("Kendaraan tidak dikenali")
        return

    struk_parkir = f"""
    _____________________________________________
    ----------------STRUK PARKIR-----------------
    _____________________________________________

    Jenis Kendaraan  {jenis_kendaraan}
    Plat Nomor  {plat_nomor}
    Lama Waktu Parkir  {durasi_parkir} jam
    Total Biaya Parkir  Rp {biaya_parkir} """
    
    print(struk_parkir)
    return struk_parkir

def simpan_struk(struk_parkir):
    file_riwayat = "riwayat.txt"
    with open(file_riwayat, "a") as file:
        file.write(struk_parkir + "\n")
    print("\nStruk berhasil disimpan ke file.")

def get_plat_nomor():
    return input("Masukkan plat nomor kendaraan: ")

def get_durasi_parkir():
    durasi = int(input("Masukkan durasi parkir dalam jam: "))
    if durasi > 0:
        return durasi
    else:
        print("Durasi parkir harus lebih dari 0.")

def get_jenis_kendaraan():
    jenis = input("Masukkan jenis kendaraan (a untuk Motor, b untuk Mobil): ").lower()
    if jenis in ['a', 'b']:
        return jenis
    else:
        print("Input tidak valid. Pilih 'a' untuk Motor atau 'b' untuk Mobil.")

def get_biaya_parkir(jenis_kendaraan, durasi_parkir):
    if jenis_kendaraan == 'a':  
        if durasi_parkir > 1:
            return 1000 + ((durasi_parkir - 1) * 1500)
        else :
            return 1000
    elif jenis_kendaraan == 'b':  
        if durasi_parkir > 1:
            return 3000 + ((durasi_parkir - 1) * 3500)
        else :
            return 3000
    