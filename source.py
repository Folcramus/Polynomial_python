from Polynomial import Polynomial


poly = Polynomial(1, 2, -3)
poly+=Polynomial(1)
print(poly)
print(poly.der(1))

