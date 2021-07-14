from dataclasses import dataclass

@dataclass
class CoffeeMachine:
    water : int
    beans : int


    def add_water(self, amount : int):
        self.water += amount


    def add_beans(self, amount : int):
        self.beans += amount

    def make_coffee(self, coffee_type : str):
        if coffee_type == "crema":
            if self.water >= 200 and self.beans >= 15:
                self.water -= 200
                self.beans -= 15
                return 200
            return 0
        return 0

cm = CoffeeMachine(0,0)
cm.add_water(450)
cm.add_beans(50)
cm.make_coffee("crema")
print(cm)
@dataclass
class MilkCoffeeMachine(CoffeeMachine):
    milk : int


    def add_milk(self,amount:int):
        self.milk += amount

    def make_coffee(self,coffee_type:str):
        if coffee_type == "latte":
            if self.water >= 150 and self.beans >= 15 and self.milk >= 50:
                self.water -= 150
                self.beans -= 15
                self.milk -= 50
                return 200
            return 0
        else:
            return super().make_coffee(coffee_type)

