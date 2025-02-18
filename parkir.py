


def get_jenis_kendaraan():
    jenis_kendaraan = input("Masukkan jenis kendaraan (a untuk Motor, b untuk Mobil): ")
    return jenis_kendaraan

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

def print_struk_parkir(jenis_kendaraan, plat_nomor, durasi_parkir, biaya_parkir):
    if jenis_kendaraan.lower() == 'a':
        print("\nJenis kendaraan: Motor")
        print("Tarif 1 jam pertama: Rp1500")
        print("Tarif jam berikutnya: Rp1000")
    else:
        print("\nJenis kendaraan: Mobil")
        print("Tarif 1 jam pertama: Rp3500")
        print("Tarif jam berikutnya: Rp3000")
    
    print(f"\nPlat nomor kendaraan: {plat_nomor}")
    print(f"Durasi parkir: {durasi_parkir} jam")
    print(f"Total biaya parkir: Rp{biaya_parkir}")

def main():
    print("=== Selamat Datang ===")
    jenis_kendaraan = get_jenis_kendaraan()
    plat_nomor = get_plat_nomor()
    durasi_parkir = get_durasi_parkir()
    biaya_parkir = get_biaya_parkir(jenis_kendaraan, durasi_parkir)

   
    print("\n=== Struk Parkir ===")
    print_struk_parkir(jenis_kendaraan, plat_nomor, durasi_parkir, biaya_parkir)

if __name__ == "__main__":
    main()