from math import *

a = int(input())

z1 = (sin(2*a) + sin(5*a) - sin(3*a)) / (cos(a) - cos(3*a) + cos(5*a))
z2 = tan(3*a)

print(ceil(z1 * 1000) / 1000, ceil(z2 * 1000) / 1000)
