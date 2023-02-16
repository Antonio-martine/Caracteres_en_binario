import pymysql as conector
import pyfiglet

def Text(text):
    font = pyfiglet.figlet_format(text)
    print(font)

def Main():
    conexion = Conectar()
    cursor = conexion.cursor()
    text = "Convertidor de caracteres a binario"
    Text(text)
    bandera = True
    while bandera == True:
        print("\nSelecciona a o b. Otro carácter será tomado como error")
        resp= input("¿Qué quieres hacer?\na) Identificar el valor de una letra o número\n"+
        "b) Identificar el valor de un texto\nc) Mostrar datos todos los datos de una tabla\n");    
        
        # Identificar el valor de una letra o numero: 
        if resp == "a":
            caracter= input("\nIdentificar:\na) Número\nb) Letra\n")
            if caracter == 'a':
                ConsultarNumero(int(input("Escribe tu número del 0 al 9:\n")),cursor)
            elif caracter == 'b':
                letra = input("Escribe tu letra (A - Z): \n")
                mayuscula = letra.upper()
                minuscula = letra.lower()
                ConsultarCaracterMinuscula(minuscula,cursor)
                ConsultarCaracterMayusculas(mayuscula,cursor)
            else: 
                print(f"Dato incorrecto, '{caracter}' no es un elemento válido")
                
        elif resp == "b":
            resp = input("\nIdentificar:\na) Cadena de texto\nb) Cadena de valores\n")
            if resp == 'a':
                Cadena_Texto(cursor)
            elif resp == 'b':
                Cadena_Digitos(cursor)
        elif resp == "c":
            tabla = input("\nObtener valores: \na) Tabla minuscula\nb) Tabla mayuscula\nc) Tabla números\n")
            if tabla == 'a':
                TablaMinusculas(cursor)
            elif tabla == 'b':
                TablaMayusculas(cursor)
            elif tabla == 'c':
                TablaNumeros(cursor)
        else:
            print(f"Dato incorrecto, '{resp}' no es un carácter válido...")
        
        continuar = input("¿Quieres continuar?\na. Si\nb.No\n")
        if continuar == 'a':
            bandera = True
        else:
            bandera = False
    conexion.close()

def Conectar():
    conectar = conector.connect(user="root",password="root", host="localhost", db="caracter_binario", cursorclass = conector.cursors.DictCursor)
    print(conectar)
    return conectar
    
def TablaMinusculas(cursor):
    cursor.execute("Select * from minusculas;")
    print("RESULTADOS DE BUSQUEDA MINUSCULAS\n") 
    for conversion in cursor.fetchall():
        contenido = FiltroMinusculas(conversion)
        print(contenido)

def TablaMayusculas(cursor):
        cursor.execute("Select * from mayusculas;")
        print("RESULTADOS DE BUSQUEDA MAYUSCULAS\n") 
        for conversion in cursor.fetchall():
            contenido = FiltroMayusculas(conversion)
            print(contenido)
                
def TablaNumeros(cursor):
        cursor.execute("Select * from numeros;")
        print("RESULTADOS DE BUSQUEDA NUMEROS\n") 
        for conversion in cursor.fetchall():
            contenido = FiltroNumeros(conversion)
            print(contenido)
    
def ConsultarCaracterMinuscula(minuscula,cursor):
    cursor.execute("Select minusculas.conversion from minusculas where letra = '"+minuscula+"'")
    for conversion in cursor.fetchall():
        digito = FiltroA(conversion)
        print(" ------------------------------------")
        print(f"|'{minuscula}' a binario = {digito} (Minúscula)|")
        print(" ------------------------------------")
    
def ConsultarNumero(numero,cursor):
    cursor.execute("Select numeros.conversion from numeros where numero = "+str(numero))
    for conversion in cursor.fetchall():
        digito = FiltroA(conversion)
        print(" ------------------------")
        print(f"|'{str(numero)}' a binario = {digito}|")
        print(" ------------------------")

def ConsultarCaracterMayusculas(mayuscula,cursor):
    cursor.execute("Select mayusculas.conversion from mayusculas where letra = '"+mayuscula+"'")
    for conversion in cursor.fetchall():
        digito = FiltroA(conversion)
        print(" ------------------------------------")
        print(f"|'{mayuscula}' a binario = {digito} (Mayúscula)|")
        print(" ------------------------------------")
        
def Cadena_Texto(cursor):
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    espacio = ' '
    
    cadena = input("Ingrese su palabra: \n")
    i, count = 0, len(cadena)
    print("\n-------------------------------------------------------")
    print(f"TEXTO A CONVERTIR: {cadena}")
    print("-------------------------------------------------------\n")
    while i < count:
        if cadena[i] in mayusculas:
            ConsultarCaracterMayusculas(cadena[i],cursor)
        elif cadena[i] in minusculas:
            ConsultarCaracterMinuscula(cadena[i],cursor)
        elif cadena[i] in espacio:
            print ('\n')
        else:
            print ('Error... no es un caracter')
            
        i=i+1
    
def Cadena_Digitos(cursor):
    numeros = '1234567890'
    espacio = ' '
    
    cadena = input("Ingrese su digitos:\n")
    i, count = 0, len(cadena)
    print("\n-------------------------------------------------------")
    print(f"TEXTO A CONVERTIR: {cadena}")
    print("-------------------------------------------------------\n")
    while i < count:
        if cadena[i] in numeros:
            ConsultarNumero(cadena[i],cursor)
        elif cadena[i] in espacio:
            print("\n")
        else:
            print ('No es un digito')
        i=i+1
    
     
    



def FiltroA(conversion):
    digito = str(conversion)
    llaves_inicio = digito.replace("{'conversion': '","")
    llaves_fin = llaves_inicio.replace("'}","")
    return llaves_fin
    
def FiltroMinusculas(conversion):
    fila = str(conversion).replace("{'id_minusculas':","")
    letra = fila.replace(", 'letra':",". Letra = ")
    conversion = letra.replace(", 'conversion':","")
    llave = conversion.replace("}","")
    return llave
    
def FiltroMayusculas(conversion):
    fila = str(conversion).replace("{'id_mayusculas':","")
    letra = fila.replace(", 'letra':",". Letra = ")
    conversion = letra.replace(", 'conversion':","")
    llave = conversion.replace("}","")
    return llave
    
def FiltroNumeros(conversion):
    fila = str(conversion).replace("{'id_numero':","")
    letra = fila.replace(", 'numero':",". Numero = ")
    conversion = letra.replace(", 'conversion':","")
    llave = conversion.replace("}","")
    return llave
    


