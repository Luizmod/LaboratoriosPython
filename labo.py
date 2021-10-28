#!/usr/bin/python3

ancho = (input("ingrese un valor "))
forma = input("ingrese un carácter ")
for i in range(int(ancho),0,-1):
	for j in range(i):
		print(forma, end="")
	print("")
