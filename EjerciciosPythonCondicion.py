#Cadena de teclado por Anthony Astudillo
import re
cadena = input("Ingrese una cadena: ")
patron = r"[A-Z]"
if re.search(patron, cadena):
    print("La cadena es una letra mayúscula.")
else:
    print("La cadena no es una letra mayúscula.")

#Algoritmo de dos notas por Anthony Astudillo
nota1 = int(input("Ingrese su nota 1: "))
nota2 = int(input("Ingrese su nota 2: "))
edad = int(input("Ingrese su edad: "))
sexo = input(("Ingrese la letra con su sexo(M:Masculino / F:Femenino): "))
if (nota1 >= 5 and nota2 >= 5) and (edad >= 18 and sexo == "F"):
    print("Aceptada.")
elif (edad >= 18 and sexo == "M"):
    print("Posible.")
else:
    print("No aceptada.")

#Ordenar de mayor a menor por Anthony Astudillo
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
if num1 > num2:
    if num2 > num3:
        print ("El orden es", num1,", ", num2,", ", num3,".")
    elif num3 > num2:
        print("El orden es", num1,", ", num3,", ", num2,".")
elif num3 > num1:
    if num1 > num2:
        print("El orden es", num3,", ", num1,", ", num2,".")
    elif num2 > num1:
        print("El orden es", num3,", ", num2,", ", num1,".")
elif num2 > num3:
    if num3 > num1:
        print("El orden es", num2,", ", num3,", ", num1,".")
    elif num1 > num3:
        print("El orden es", num2,", ", num1,", ", num3,".")

#Tipo de triangulo por Anthony Astudillo
A = float(input("Ingrese la longitud del primer lado: "))
B = float(input("Ingrese la longitud del segundo lado: "))
C = float(input("Ingrese la longitud del tercer lado: "))
if (pow(A,2)+pow(B,2)) == pow(C,2) or (pow(A,2)+pow(C,2)) == pow(B,2) or (pow(B,2)+pow(C,2)) == pow(A,2):
    print("El triángulo es rectángulo.")
elif A == B and B == C:
    print("El triángulo es equilátero.")
elif A == B or B == C or A == C:
    print("El triángulo es isósceles.")
elif A != B and B != C and A != C:
    print("El triángulo es escaleno.")
else:
    print("Los datos ingresados no corresponden a un triángulo.")

#Vinicultores por Anthony Astudillo
precio = 0
precio = float(input("Ingrese el precio por kilo de cada uva: "))
kilo = float(input("Ingrese la cantidad de kilos de uva: "))
tipo = input("Ingrese el tipo de uva (a / b): ")
tamano = int(input("Ingrese el tamaño de la uva (1 / 2): "))
precioInicial = precio * kilo
precio2 = 0 
if tipo == "a":
    if tamano == 1:
        precio2 = precioInicial + 0.20
    else:
        precio2 = precioInicial + 0.30
elif tipo == "b":
    if tamano == 1:
        precio2 = precioInicial - 0.30
    else:
        precio2 = precioInicial - 0.50
print("El precio total es: ", precio2)

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