#Ejercicio 1 perimetro y area de Anthony Astudillo
import math
base= int(input("Ingrese el valor de la base: "))
altura=int(input("Ingrese el valor de la altura: "))
radio=int(input("Ingrese el valor del radio: "))
perimetro= (base*2)+(altura*2)
area= base*altura
areaC= math.pi*(radio**2)
perimetroC= 2*math.pi*radio
print("El perimetro del rectangulo es de: ", perimetro)
print("El area del rectangulo es de: ", area)   
print("El area del circulo es de: ", areaC)
print("El perimetro del circulo es de: ", perimetroC)

#Temperatura por Anthony Astudillo
temp= float(input("Ingrese la temperatura en grados Fahrenheit: "))
tempCelsius= (temp-32)*5/9
print("La temperatura en grados Celsius es de: ", tempCelsius)

#Tiempo por Anthony Astudillo
tiempo= int(input("Ingrese una cantidad de minutos: "))
hora= tiempo//60
minutos= tiempo%60
print(tiempo,"minutos son ",hora,"horas y ",minutos,"minutos")

#Comisiones por Anthony Astudillo
sueldo = float(input("Ingrese su sueldo base: "))
venta1 = float(input("Ingrese el valor de la primera venta: "))
venta2 = float(input("Ingrese el valor de la segunda venta: "))
venta3 = float(input("Ingrese el valor de la tercera venta: "))
comisiones = (venta1 + venta2 + venta3) * 0.1 
total = sueldo + comisiones  
print("Obtendrá por comisiones un total de:", comisiones)
print("El total que recibirá es de:", total)

#Nota Final por Anthony Astudillo
parcial1 = float(input("Ingrese la nota del parcial 1: "))
parcial2 = float(input("Ingrese la nota del parcial 2: "))
parcial3 = float(input("Ingrese la nota del parcial 3: "))
examenF= float(input("Ingrese la nota del examen final: "))
trabajoF=float(input("Ingrese el nota del trabajo final: "))
promParcial= (parcial1+parcial2+parcial3)/3
notaFinal= (promParcial*0.55)+(examenF*0.3)+(trabajoF*0.15)
print("La nota final en la materia de Algoritmos es de: ", notaFinal)

#Distancia por Anthony Astudillo
import math
x1= float(input("Ingrese la coordenada x1: "))
y1= float(input("Ingrese la coordenada y1: "))
x2= float(input("Ingrese la coordenada x2: "))
y2= float(input("Ingrese la coordenada y2: "))
distancia= math.sqrt ((x2-x1)**2 + (y2-y1)**2)
print("La distancia entre los puntos es: ", distancia)

#Numero invertido por Anthony Astudillo
num= int(input("Ingrese un numero de 2 cifras: "))
decena= num//10
unidad= num%10
inverso= (unidad*10)+decena
print("El numero invertido es: ", inverso)

#Velocidades por Anthony Astudillo
import math
v1= float(input("Ingrese la velocidad del primer coche: "))
v2= float(input("Ingrese la velocidad del segundo coche: "))
d= float(input("Ingrese la distancia entre los dos coches: "))
if v1>v2:
    t=d/(v1-v2)
elif v1<v2:
    t=d/(v2-v1)
else:
    print("Los coches tienen la misma velociad, no se acercan ni se alejan")
tiempo=t*60
print("El tiempo que tardaran en encontrarse es de: ", tiempo, "minutos")

#Iniciales por Anthony Astudillo
nombre= input("Ingrese su nombre: ")
apellido1= input("Ingrese su primer apellido: ")
apellido2= input("Ingrese su segundo apellido: ")
inicialnombre= nombre[0]
inicialapellido1= apellido1[0]
inicialapellido2= apellido2[0]
iniciales= inicialnombre+inicialapellido1+inicialapellido2
print("Sus iniciales son: ", iniciales)

#Dinero por Anthony Astudillo
dosEuros= float(input("Ingrese la cantidad de monedas de 2 euros: "))
unEuro= float(input("Ingrese la cantidad de monedas de 1 euro: "))
cincuentaC= float(input("Ingrese la cantidad de monedas de 50 centimos: "))
veinteC= float(input("Ingrese la cantidad de monedas de 20 centimos: "))
diezC= float(input("Ingrese la cantidad de monedas de 10 centimos: "))
totalE= (dosEuros*2)+(unEuro*1)+(cincuentaC*0.5)+(veinteC*0.2)+(diezC*0.1)
print("El total de dinero que tiene en euros: ", totalE)

#Programa que determina el pago al autobus y de los alumnos por Anthony Astudillo
alumnos = int(input("Escriba cuantos alumnos van a ir: "))
if alumnos >= 100:
    print ("El costo por alumno es de: ", 65,"euros")
    print ("El valor de la renta al autobus es: ", alumnos * 65,"euros")
elif alumnos >= 50 and alumnos <= 99:
    print ("El costo por alumno es de: ", 70,"euros")
    print ("El valor de la renta al autobus  es: ", alumnos * 70,"euros")
elif alumnos >= 30 and alumnos <= 49:
    print ("El costo por alumno es de: ", 95,"euros")
    print ("El valor de la renta al autobus es: ", alumnos * 95,"euros")
else:
    print ("El valor de la renta al autobus es : ", 4000,"euros")

#Programa que da el precio del paquete y si es rechazado por Anthony Astudillo
print ("Contienente que se puede ir:")
print ("1:America del Norte")
print ("2:America del Central")
print ("3:America del Sur")
print ("4:Europa")
print ("5:Asia")
opciones = input("Seleccione el numero del contienente a enviar:")
peso = float(input("Escriba cuanto peso tiene su paquete en kg: "))
if peso > 5:
    print ("El paquete es muy pesado no puede viajar")
elif opciones == "1":
    print ("El costo por America del Norte es de: ", 24,"euros")
    print ("El valor total que debe pagar es de: ", peso * 24,"euros")
elif opciones == "2":
    print ("El costo por America del Central es de: ", 20,"euros")
    print ("El valor total que debe pagar es de: ", peso * 20,"euros")
elif opciones == "3":
    print ("El costo por America del Sur es de: ", 21,"euros")
    print ("El valor total que debe pagar es de: ", peso * 21,"euros")
elif opciones == "4":
    print ("El costo por Europa es de: ", 10,"euros")
    print ("El valor total que debe pagar es de: ", peso * 10,"euros")
elif opciones == "5":
    print ("El costo por Asia es de: ", 18,"euros")
    print ("El valor total que debe pagar es de: ", peso * 18,"euros")
else:
    print ("El valor no es valido")

#Programa que determina el dia de la semana por Anthony Astudillo
dia = input("Escriba un numero para descubrir que dia de la semana es: ")
if dia == "1":
    print ("El dia es Lunes")
elif dia == "2":
    print ("El dia es Martes")
elif dia == "3":
    print ("El dia es Miercoles")
elif dia == "4":
    print ("El dia es Jueves")
elif dia == "5":
    print ("El dia es Viernes")
elif dia == "6":
    print ("El dia es Sabado")
elif dia == "7":
    print ("El dia es Domingo")
else:
    print ("Valor invalido")

#Programa que indica el tipo de motor por Anthony Astudillo
print ("Los tipos de motores son:")
print ("1:Motor")
print ("2:Motor")
print ("3:Motor")
print ("4:Motor")
print ("5:Motor")
opciones = input("Seleccione el tipo de motor que desea:")
if opciones == "0":
    print ("No hay establecido un valor definido para el tipo de bomba")
elif opciones == "1":
    print ("La bomba es una bomba de agua")
elif opciones == "2":
    print ("La bomba es una bomba de gasolina")
elif opciones == "3":
    print ("La bomba es una bomba de hormigón")
elif opciones == "4":
    print ("La bomba es una bomba de pasta alimenticia")
else:
    print ("No existe un valor válido para tipo de bomba")

#Programa de notas de ingles por Anthony Astudillo
nombre = input("Ingrese el nombre del estudiante: ")
nota = float(input("Ingrese la nota de ingles: "))
if nota>9 and nota<=10:
    print("Felicitaciones", nombre, "su nota es",nota, "equivalente a excelente")
elif nota>7 and nota<=8:
     print("Siga adelante", nombre,"su nota es", nota,"equivalente a muy buena")
elif nota>5 and nota<=6:
    print("Debe esforzarse más", nombre,"su nota es", nota,"equivalente a buena")
elif nota>0 and nota<=4:
    print("Usted", nombre,"puede reprobar ya que su nota es", nota,"equivalente a regula")
else:
    print("Valor invalido")