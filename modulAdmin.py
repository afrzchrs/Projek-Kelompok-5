def riwayat():
    file = open("riwayat.txt", "r")
    b = file.read().splitlines()  
    b.sort()  
    print(b)