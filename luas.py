#NAMA : JULIANTI
#NIM : D0221077

def line():
    print("="*50)
    
def enter():
    print("\n")
    
def menu():
    while True:
        enter()
        line()
        print(" PROGRAM MENGHITUNG LUAS BIDANG DATAR ".center(50,"-"))
        print("1. Menghitung Luas Persegi")
        print("2. Menghitung Luas Lingkaran")
        print("3. Menghitung Luas Segitiga")
        print("4. Keluar")
        line()
        menu = input("Masukkan Pilihan (1/2/3/4): ").lower()
        if menu == "1" or menu == "persegi":
            persegi()
        elif menu == "2" or menu == "lingkaran":
            lingkaran()
        elif menu == "3" or menu == "segitiga":
            segitiga()
        elif menu == "4" or menu == "keluar":
            enter()
            print(" EXIT ".center(50,"="))
            exit()
            
        else:
            print("Pilihan Tidak Tersedia. Mohon Coba Lagi!")
            enter()
    
def persegi():
    enter()
    line()
    print(" MENGHITUNG LUAS PERSEGI ".center(50,"-"))
    sisi = int(input("Masukkan Panjang Sisi Persegi: "))
    luas_persegi = sisi*sisi
    print("Luas Persegi : ", luas_persegi, " cm²")
    line()
    menu() 

def lingkaran():
    enter()
    line()
    print(" MENGHITUNG LUAS LINGKARAN ".center(50,"-"))
    jari_jari = int(input("Masukkan Panjang Jari-Jari Lingkaran: "))
    luas_lingkaran = 3.14 * jari_jari ** 2
    print("Luas Lingkaran: ", luas_lingkaran, " cm²")
    line()
    menu()
    
def segitiga():
    enter()
    line()
    print(" MENGHITUNG LUAS SEGITIGA ".center(50,"-"))
    alas_segitiga = int(input("Masukkan Panjang Alas Segitiga: "))
    tinggi_segitiga = int(input("Masukkan Tinggi Segitiga: "))
    luas_segitiga = 1/2 * alas_segitiga * tinggi_segitiga
    print("Luas Segitiga: ", luas_segitiga, " cm²")
    line()
    menu()
    
menu()
