#Autor Oscar Sandoval

#clase introduccion a objetos y clases

#Ejercicio de poner feliz/triste al perro

class Perro:
    def __init__(self, Nombredelperro):
        self.nombre = Nombredelperro
    def perrofeliz(self):
        print(f"{self.nombre} está feliz.")
    def perrotriste(self):
        print(f"{self.nombre} está triste.")

Nombredelperro = input("¿Cual es el nombre del perro?: ")
perro1 = Perro(Nombredelperro)

accion = int(input("Que accion desea realizar?:\n1. Acariciar\n2. Darle comida\n3. No hacer nada\n---> "))
verific = type(accion)
verific == int
while verific == False:
    print("Accion no válida, elije otra.")
    accion = int(input("Que accion desea realizar?:\n1. acariciar\nNo hay mas opciones...\n3. No hacer nada\n--> "))
while accion < 1 or accion > 3:
    print("Accion no válida, elije otra.")
    accion = int(input("Que accion desea realizar?:\n1. acariciar\nNo hay mas opciones...\n3. No hacer nada\n--> "))
if accion == 1 or accion == 2:
    perro1.perrofeliz()
elif accion == 3:
    perro1.perrotriste()