import sqlite3

class Hayvan:
    def __init__(self):
        self.con = sqlite3.connect("Grup_Listeleri.db")
        self.cursor = self.con.cursor()

    def ekleme(self, Grupİsmi, HayvanTasmaNumara, Hayvanİsim, HayvanYas, HayvanTürü):
        self.cursor.execute("INSERT INTO {grup_ismi} VALUES(?,?,?)".format(grup_ismi = Grupİsmi),
                            (HayvanTasmaNumara, Hayvanİsim, HayvanYas, HayvanTürü))

Hayvan = Hayvan()