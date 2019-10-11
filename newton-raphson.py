import sympy as sp
import math as mt
x=sp.Symbol('x')
aux = input('ingrese la ecuacion :  ')
ecu = sp.simplify(aux)
print(ecu)
ecudif = sp.diff(ecu,x)
xi = int(input('inserte xi :  '))
x1 = xi+1

while mt.fabs(mt.fabs(xi)-mt.fabs(x1)) > 0.004 or mt.fabs(mt.fabs(x1)-mt.fabs(xi)) > 0.00004:
	x1 = xi
	xi = xi -(ecu.subs(x,xi)/ecudif.subs(x,xi))
	print(sp.N(xi))
