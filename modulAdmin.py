import os
def riwayat():
    os.system('cls')
    with open("riwayat.txt", "r") as file:
                b = file.read().splitlines()
                b.sort()
                for line in b:
                    print(line)
    
    kembali = input("\n\nkembali?:(Y/y)").lower()
    if kembali == 'y':
        return
