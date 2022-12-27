#NAMA : JULIANTI
#NIM : D0221077

class Kubus():
    def __init__(self, s):
        self.s = s

    def volume(self):
        v_kubus = self.s**3
        print("volume kubus : ", v_kubus)

    def luas(self):
        l_kubus = 6 * self.s**2
        print("luas permukaan kubus : ", l_kubus)

class Balok():
    def __init__(self, p, l, t):
        self.p = p
        self.l = l
        self.t = t

    def volume(self):
        v_balok = self.p * self.l * self.t
        print("Volume balok : ", v_balok)

    def luas(self):
        l_balok = 2 * (self.p * self.l + self.p * self.t + self.l * self.t)
        print("luas permukaan balok : ", l_balok)

class Tabung():
    def __init__(self, r, t):
        self.r = r
        self.t = t

    def volume (self):
        v_tabung = 22/7 * self.r**2 * self.t
        print("volume tabung : " , round(v_tabung,2))

    def luas (self):
        l_tabung = 2 * 22/7 * self.r * self.t + 2 * 22/7 * self.r**2
        print("luas perrmukaan tabung : ", round(l_tabung,2))

class Limas():
    def __init__(self, a, tA, t):
        self.a = a
        self.tA = tA
        self.t = t

    def volume (self):
        v_limas = 1/3 * 1/2 * self.a * self.tA * self.t
        print("volume limas segitiga : " , round(v_limas,2))

    def luas (self):
        l_limas = 1/2 * self.a * self.tA + ( 3 * 1/2 * self.a * self.tA)
        print("luas limas segitiga : ", round(l_limas,2))

while True:
    print()
    print(" SELAMAT DATANG DI MENU MENGHITUNG VOLUME DAN LUAS PERMUKAAN BANGUN RUANG ")
    print("--------------------------------------------------------------------------")
    print()
    print("""silahkan pilih Bangun Ruang yang akan dihitung :
1. Kubus
2. Balok
3. Tabung
4. Limas Segitiga
5. Finish""")
    menu = input("masukkan pilihan : ")
    print()

    if menu == '1':
        s = float(input("masukkan sisi : "))
        kubus = Kubus(s)
        print()
        kubus.volume()
        kubus.luas()

    elif menu == '2':
        p = float(input("masukkan panjang : "))
        l = float(input("massukkan lebar : "))
        t = float(input("masukkan tinggi : "))
        balok = Balok(p,l,t)
        print()
        balok.volume()
        balok.luas()

    elif menu == '3':
        j = float(input("masukkan jari-jari : "))
        t = float(input("masukkan tinggi : "))
        tabung = Tabung (j,t)
        print()
        tabung.volume()
        tabung.luas()
        
    elif menu == '4':
        a = float(input("masukkan alas : "))
        tA = float(input("masukkan tinggi alas : "))
        t = float(input("masukkan tinggi : "))
        limas = Limas (a,tA,t)
        print()
        limas.volume()
        limas.luas()

    elif menu == '5':
        break

    else:
        print("""Maaf pilihan Anda salah.
Silahkan masukkan kembali pilihan anda.""")

