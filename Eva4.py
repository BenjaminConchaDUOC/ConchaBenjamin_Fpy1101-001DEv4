#ConchaBenjamin_Fpy1101-001DFv4

import os
os.system("cls")
usuarios=[]


def ingreso():
    while True:

        newUser=input("Ingrese nombre de usuario: ")
        if newUser in usuarios:
            print("Usuario ya existe. Intente otro.")
        
        else:
            while True:
                sexo=input("Ingrese sexo M, F o C : ").upper()
                if sexo == "M":
                   break
                elif sexo =="F":
                    break
                elif sexo =="C":
                    break
                else:
                    print("Debe ingresar M, F o C solamente. Intente de nuevo.")
            
            while True:
                pw= input("Ingrese contraseña: ")
                break
        
        usuarios.append(newUser)
        usuarios.append(sexo)
        usuarios.append(pw)

        print("Usuario ingresado con exito!!")
        break
                
                       
def buscar():
    busqueda=input("Ingrese usuario a buscar: ")
    if busqueda in usuarios:
        print("Usuario encontrado")
        for encontrado in usuarios:
            print(f"usuario{usuarios}")

    
    else: 
        print("usuario no encontrado")


def eliminar():
    while True:
        delete=input("Ingrese usuario a buscar: ")
        if delete in usuarios:
            usuarios.remove(delete)
            print(f"usuario eliminado")
            break
            
        else:
            print("usuario no existe")
        







while True:
    print("""MENU PRINCIPAL
    1.-Ingresar usuario
    2.-Buscar usuario
    3.-Eliminar usuario
    4.-Salir""")
    try:
        opcion=input("ingrese una opcion: ")
        
    except:
        print("Debe ingresar una opción válida!!")
    
    if opcion == "1":

        ingreso()
    
    elif opcion == "2":

        buscar()
    
    elif opcion == "3":
        
        eliminar()
    
    elif opcion == "4":
        print("programa terminado")
        break
    
    else:
        print("Opcion invalida")

    