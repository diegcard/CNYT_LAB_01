import math
def sumcomplex(c1,c2):
    real = c1[0] + c2[0]
    imag = c1[1] + c2[1]
    return (real,imag)

def restcomplex(c1,c2):
    real = c1[0] - c2[0]
    imag = c1[1] - c2[1]
    return (real,imag)

def multcomplex(c1,c2):
    real = (c1[0] * c2[0]) - (c1[1] * c2[1])
    imag = (c1[0] * c2[1]) + (c1[1] * c2[0])
    return (real,imag)

def divcomplex(c1,c2):
    real = round(((c1[0] * c2[0]) + (c1[1] * c2[1])) / ((c2[0]**2) + (c2[1]**2)),2)
    imag = round(((c2[0] * c1[1]) - (c1[0] * c2[1])) / ((c2[0]**2) + (c2[1]**2)),2)
    return (real,imag)

def moducomplex(c):
    return round(math.sqrt((c[0] ** 2) + (c[1] ** 2)),2)

def conjucomplex(c):
    return (c[0], -1 * c[1])

def cartesian_to_polar_complex(c):
    x = c[0]
    y = c[1]
    r = round(math.sqrt(x**2 + y**2),2)
    theta = round(math.atan2(y, x))
    return (r, theta)

def fasecomplex(c):
    return round(math.atan2(c[1],c[0]),2)