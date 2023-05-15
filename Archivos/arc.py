file = open("./Archivos/EjemploArchivo.txt", "w")
file.write("Este es el contenido del archivo")
file.close()

lista = ["Fresa", "Kiwi", "Papaya"]
with open ("EjemploArchivo.txt", "a") as file:
    for e in lista:
        file.write(e + "\n")
        
        
print("Archivo escrito")

lista2 = ["Honda", "Nisan", "Toyota"]

with open ("EjemploArchivo.txt", "a") as file:
    file.writelines(lista2)
    
print("Lista escrita con con writelines")