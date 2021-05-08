def Menu():
    print('----MENU----')
    print('1) Suma\n 2) Resta\n 3) Multiplicacion\n 4) Division\n 5) Salir')

def Calculadora():
    print("""Funcion Para Calcular Operaciones Aritmeticas""")
    Menu()
    opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <5):
        x = int(input("Ingrese Numero\n"))
        y = int(input("Ingrese Otro Numero\n"))
        if (opc==1):
            print ("La Suma es:", x+y)
            opc = int(input("Selecione Opcion\n"))
        elif(opc==2):
            print ("La Resta es:",x-y)
            opc = int(input("Selecione Opcion\n"))
        elif(opc==3):
            print ("La Multiplicacion es:",x*y)
            opc = int(input("Selecione Opcion\n"))
        elif(opc==4):
            try:
              print ("La Division es:", x/y)
              opc = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
              print ("No se Permite la Division Entre 0")
              opc = int(input("Selecione Opcion\n"))
Calculadora()
