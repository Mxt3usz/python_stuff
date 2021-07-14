import math

def rgb(r,g,b):
    if r > 255:
        r = 255
    if r < 0:
        r = 0
    if g > 255:
        g = 255
    if  g < 0 :
        g = 0
    if b > 255:
        b = 255
    if b < 0 :
        b = 0
    red = r
    green = g
    blue = b
    r = math.floor(r/16)
    g = math.floor(g/16)
    b = math.floor(b/16)
    res = ""
    res_r = red - 16 * r
    res_g = green - 16 * g
    res_b = blue  - 16 * b
    if r == 10:
        r = "A"
    if type(r) is int and r == 11:
        r = "B"
    if type(r) is int and r == 12:
        r = "C"
    if type(r) is int and r == 13:
        r = "D"
    if type(r) is int and r == 14:
        r = "E"
    if type(r) is int and r == 15:
        r = "F"
    if g == 10:
        g = "A"
    if type(g) is int and g == 11:
        g = "B"
    if type(g) is int and g == 12:
        g = "C"
    if type(g) is int and g == 13:
        g = "D"
    if type(g) is int and g == 14:
        g = "E"
    if type(g) is int and g == 15:
        g = "F"
    if b == 10:
        b = "A"
    if type(b) is int and b == 11:
        b = "B"
    if type(b) is int and b == 12:
        b = "C"
    if type(b) is int and b == 13:
        b = "D"
    if type(b) is int and b == 14:
        b = "E"
    if type(b) is int and b == 15:
        b = "F"
    if res_r == 10:
        res_r = "A"
    if type(res_r) is int and res_r == 11:
        res_r = "B"
    if type(res_r) is int and res_r == 12:
        res_r = "C"
    if type(res_r) is int and res_r == 13:
        res_r = "D"
    if type(res_r) is int and res_r == 14:
        res_r = "E"
    if type(res_r) is int and res_r == 15:
        res_r = "F"
    if res_g == 10:
        res_g = "A"
    if type(res_g) is int and res_g == 11:
        res_g = "B"
    if  type(res_g) is int and res_g == 12:
        res_g = "C"
    if type(res_g) is int and res_g  == 13:
        res_g = "D"
    if type(res_g) is int and res_g == 14:
        res_g = "E"
    if type(res_g) is int and res_g == 15:
        res_g = "F"
    if res_b == 10:
        res_b = "A"
    if type(res_b) is int and res_b == 11:
        res_b = "B"
    if type(res_b) is int and res_b == 12:
        res_b = "C"
    if type(res_b) is int and res_b == 13:
        res_b = "D"
    if type(res_b) is int and res_b == 14:
        res_b = "E"
    if type(res_b) is int and res_b == 15:
        res_b = "F"
    res += str(r)
    res += str(res_r)
    res += str(g)
    res += str(res_g)
    res += str(b)
    res += str(res_b)
    return str(res)


