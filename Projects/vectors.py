from dataclasses import dataclass

@dataclass
class V3:
    x : int
    y : int
    z : int
cadd = lambda v, w: V3(v.x + w.x, v.y + w.y, v.z + w.z)
cmul = lambda v, w: V3(v.x * w.x, v.y * w.y, v.z * w.z)

map2 = lambda x: lambda v,w: V3(x(v.x,w.x),x(v.y,w.y),x(v.z,w.z))

addV = map2(lambda x,y: x + y)
mulV = map2(lambda x,y: x * y)
print(map2(lambda x,y: x +y)(V3(1,2,3),V3(2,5,6)))
