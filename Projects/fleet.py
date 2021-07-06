from dataclasses import dataclass

@dataclass
class Fahrzeug:
    leergewicht : int
    baujahr : int
    def show_type(self):
        return self.__class__.__name__
    def show_data(self):
        return "Leergewicht:" + " " + str(self.leergewicht) + "kg" + " "+ "Baujahr:" + " " + str(self.baujahr)
    def show(self):
        return show_type() + " " + self.show_data()
@dataclass
class Kraftfahrzeug(Fahrzeug):
    leistung : int
    sitz : int
    def show_data(self):
        return super().show_data() + " " + "Leistung:" + " " + str(self.leistung) + "kW"+ " " + "Sitzplätze:" + " " + str(self.sitz)
    def show(self):
        return super().show_type() + " " + self.show_data()
@dataclass
class Bus(Kraftfahrzeug):
    steh : int
    def show_data(self):
        return super().show_data() + " " + "Stehplätze:" + " " + str(self.steh)
    def show(self):
        return super().show_type() + " " + self.show_data()
@dataclass
class Fahrrad(Fahrzeug):
    rahmen : int
    def show_data(self):
        return super().show_data() + " " + "Rahmengröße:" + " " + str(self.rahmen) + "cm"
    def show(self):
        return super().show_type() + " " + self.show_data()
@dataclass
class PKW(Kraftfahrzeug):
    pass

@dataclass
class LKW(Kraftfahrzeug):
    zuladung : int
    def show_data(self):
        return super().show_data() + " " + "Zuladung:" + " " + str(self.zuladung) + "kg"
    def show(self):
        return super().show_type() + " " + self.show_data()

rad = Fahrrad(10, 2019, 55)
print(rad.show_type())
print(rad.show_data())
print(rad.show())
pkw = PKW(1200, 2016, 90, 5)
print(pkw.show())
lkw = LKW(1200, 2016, 100, 2, 200)
print(lkw.show())
bus = Bus(2000, 2015, 100, 40, 10)

def maut(fzg: Fahrzeug) -> int:
    if isinstance(fzg, Fahrrad):
        return 0
    if isinstance(fzg, LKW):
        return (fzg.leergewicht + fzg.zuladung) // 10 + fzg.sitz * 20
    if isinstance(fzg, Bus):
        return fzg.leergewicht // 10 + (fzg.sitz + fzg.steh) * 20
    if isinstance(fzg, Kraftfahrzeug):
        return  fzg.leergewicht // 10 + fzg.sitz * 20

print(maut(pkw))
print(maut(lkw))
print(maut(bus))
