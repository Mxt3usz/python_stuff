from dataclasses import dataclass

@dataclass
class Robot:
    hp : int
    armor : int
    attack :int
    robot_typ: int

    def __post_init__(self):
        assert(self.robot_typ >0 and self.robot_typ < 4)

    def hit_damage(self,other):
        if self.attack == 0 :
            self.attack == 1
        if self.robot_typ == 1 and other.robot_typ == 2:
            self.attack + 1 - other.armor + 2
        if self.robot_typ == 1 and other.robot_typ == 3:
            self.attack + 2 - other.armor
        else:
            self.attack - other.armor

r1 = Robot(10,1,1,1)
r2 = Robot(10,1,1,1)
a = r1.hit_damage(r2)
print(r2)
