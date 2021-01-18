#Escribe un programa que pida un nombre de usuario y una contraseña y
#si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”,
#sino se da un error.

logNom = input("Introduzca un usuario")
usuario = "Kentu"
logPass = int(input("Introduzca una constraseña"))
password = 1234

if logNom == usuario and logPass == password:
    print("Credenciales correctas. Has entrado al sistema")
elif logNom != usuario or logPass != password:
    print("Usuario o contraseña incorrectos")
else:
    print("Fin del programa")
