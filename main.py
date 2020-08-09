import gruplar, hayvan
import random

while True:
    tercih = input("HOŞGELDİNİZ! \n "
                   "Grup eklemek için C'ye tıklayın. \n "
                   "Hayvan eklemek için S'ye tıklayın: \n"
                   "Çıkış için Q'ya  tıklayınız: \n")

    if tercih == "Q" or tercih == "q":
        print("Tekrar bekleriz!")
        break

    else:
        Grupİsmi = input("Grup ismini giriniz: ")

        if tercih == "C" or tercih == "c":
            gruplar.Grup.ekleme(Grupİsmi)

        elif tercih == "S" or tercih == "s":
            HayvanTasmaNumara = random.randint(200,400)
            HayvanIsim = input("Hayvan ismini giriniz: ")
            HayvanYas = int("Hayvan yaşını giriniz: ")
            HayvanTürü=input("Hayvan türünü giriniz: ")
            hayvan.Hayvan.ekleme(Grupİsmi,HayvanTasmaNumarası, HayvanIsim, HayvanYas, HayvanTürü)