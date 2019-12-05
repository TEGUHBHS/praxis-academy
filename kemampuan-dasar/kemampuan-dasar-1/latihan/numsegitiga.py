print("-"*50)
print(" ")
string = ""
angka = int(input("masukkan = "))
nomor = angka
    while angka >= 0:
    kolom = angka
        while kolom > 0:
            string = string + " " + str(nomor) + " "
            kolom = kolom - 1
        string = string + "\n"
        angka = angka - 1
        nomor = nomor - 1
print (string)