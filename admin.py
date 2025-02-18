with open("riwayat.txt", "r") as file:
    b = file.read().splitlines()  

b.sort()  
print(b)
