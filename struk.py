# Function untuk menampilkan struk parkir
def tamp_struk_parkir (jenis_kendaraan, plat_nomor, durasi_parkir, biaya_parkir):
    if jenis_kendaraan.lower() == 'a':
        jenis_kendaraan = "Motor" 
    elif jenis_kendaraan.lower() == 'b':
        jenis_kendaraan = "Mobil" 
    else : 
        print("Kendaraan tidak dikenali")

    struk_parkir = f"""
    _____________________________________________
    ----------------STRUK PARKIR-----------------
    _____________________________________________

    Jenis Kendaraan : {jenis_kendaraan}
    Plat Nomor : {plat_nomor}
    Lama Waktu Parkir : {durasi_parkir} jam
    Total Biaya Parkir : Rp {biaya_parkir} """
    
    print(struk_parkir)
    return struk_parkir

def simpan_struk (struk_parkir) : 
    # Simpan struk ke file
    file_riwayat = "riwayat.txt"
    try:
        with open(file_riwayat, "a") as file:
            file.write(struk_parkir + "\n" )
        print("\nStruk berhasil disimpan ke file.")
    except IOError:
        print("Gagal membuka file untuk mencetak struk.")
