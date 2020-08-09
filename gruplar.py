import sqlite3


class Grup:
    def __init__(self):
        self.con = sqlite3.connect("Grup_Listeleri.db")
        self.cursor = self.con.cursor()

    def ekleme(self, GrupIsmi):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS {grup_ismi}"
                            "(HayvanTasmaNumara INT, "
                            "HayvanIsim TEXT, "
                            "HayvanYas INT, "
                            "HayvanTürü TEXT)".format(grup_ismi=GrupIsmi))


Grup = Grup()
