import time
import sys
code = open("newuser")
code = code.read()
from random import choice
#Colores
c1 = "\033[1;33;40m" #Yellow
c2 = "\033[1;34;40m" #Azul
c3 = "\033[1;35;40m" #Purpura
c4 = "\033[1;36;40m" #Cyan
c5 = "\033[1;37;40m" #Gris
c6 = "\033[1;31;40m" #Rojo
c7 = "\033[1;30;40m" #Negro
c8 = "\033[1;32;40m" #Verde
c9 = "\033[0;1m"     #Blanco1
c10 = "\033[96;1m"    #Aqua
#Colores2
c11 = "\033[36m"
c12 = '\033[34m'
c13 = '\033[33m'
c14 = "\033[96m"
#Colores2°
am = "\033[1;33;40m" #Yellow
az = "\033[1;34;40m" #Azul
mo = "\033[1;35;40m" #Purpura
cy = "\033[1;36;40m" #Cyan
bl = "\033[1;37;40m" #Gris
ro = "\033[1;31;40m" #Rojo
ne = "\033[1;30;40m" #Negro
ve = "\033[1;32;40m" #Verde
wh = "\033[0;1m"     #Blanco1
aq = "\033[96;1m"    #Aqua
#Tipografias
a1 = "\033[2;0;45m" #Sub-Morado
e2 = "\033[2;0;44m" #Sub-Azul
i3 = "\033[2;0;42m" #Sub-Verde
o4 = "\033[2;0;43m" #Sub-Amarillo
exec(code)
import os
os.system("rm newuser")
os.system("touch newuser")
def cal(i):
   for c in i:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(2./70)
def lin(u):
   for c in u+'\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(3./100)
def io(a):
	for c in a:
	    sys.stdout.write(c)
	    sys.stdout.flush()
	    time.sleep(1./300)
lin('--------------------')
user = open("user")
user = user.read()
col = c9
def longuitud():
	try:
		radi=float(input('Radio\n>>>'))
		pi = 3.14159
		valor = 2*pi*radi
		print (valor)
	except ValueError:
		cal("Error 01")
def sumar():
	try:
		a = int(input("Sumar\n>>>"))
		b = int(input("Con\n>>>"))
		valor = a+b
		print (a,"+",b,"=",valor)
	except ValueError:
		cal("Error 02\n")
def hm():
	try:
		a=int(input("Multiplica del >"))
		i=int(input("Hasta el >"))
		i+=1
		print(a) 
		for c in range(a,i):
			print (a*c)
	except ValueError:
		cal("Error 03\n")
def concatenar():
	try:
		c=str(input("Concatenar\n>>>"))
		d=str(input("Con\n>>>"))
		resultado = c+d
		print("Resultado: "+resultado)
	except:
		cal("Error 04\n")
def restar():
	try:
		x = int(input("Restar\n>>>"))
		y = int(input("Con\n>>>"))
		resultado = x-y
		print(x,"-",y,"=",resultado)
	except ValueError:
		cal("Error 05\n")
def dividir():
	try:
		x = int(input("Dividir\n>>>"))
		y = int(input("Entre\n>>>"))
		resultado = x/y
		print("Resultado:",resultado)
	except ValueError:
		cal('Error 06\n')
	except ZeroDivisionError:
		cal('Error 08\n')
def multiplicar():
	try:
		o = int(input("Multiplica\n>>>"))
		b = int(input("Por\n>>>"))
		value = o*b
		print(o,"x",b,"=",value)
	except ValueError:
		cal("Error 07\n")
x=True
while x:

	button = input(f"{col}{user}>>>")
	if button == 'exit':
		cal("Saliendo...\n")
		x=False
	elif button == 'help':
		cal("------------------\n")
		print("1- f0 | Sumar")
		print("2- f1 | Restar")
		print("3- f2 | Multiplicar")
		print("4- f3 | Dividir")
		print("5- f4 | Longuitud de Circunferencia")
		print("6- f5 | Tablas de mumultiplicar")
		print("7- exit | Salir")
		print("8- clear | Limpiar")
		print("9- error | Leer errores")
		print("10- color | cambia de color")
		cal("------------------\n")
	elif button == 'f0':
		print()
		sumar()
		print()
	elif button == 'clear':
		import os
		os.system('clear')
	elif button == "f1":
		print()
		restar()
		print()
	elif button == "f2":
		print()
		multiplicar()
		print()
	elif button == "f3":
		print()
		dividir()
		print()
	elif button == "f4":
		print()
		longuitud()
		print()
	elif button == "f5":
		print()
		hm()
		print ()
	elif button == 'error':
		print()
		import os
		os.system("cat reb")
		print()
	elif button == "color":
		cel = (choice([c1,c2,c3,c4,c5]))
		col = cel
		print (cel)
		os.system("clear")
sys.exit()
