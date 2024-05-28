from multiprocessing import Process
import random

def proceso1(nombreArchivo):
    with open(nombreArchivo, "w") as archivo:
        for i in range(6):
            nota = round(random.uniform(1,10), 2) 
            archivo.write(str(nota)+"\n")

def proceso2(nombreArchivo, nombreAlumno):
    suma = 0
    with open(nombreArchivo, "r") as archivo:
        for notaCadena in archivo.readlines():
            suma += float(notaCadena)
    
    media = round(suma/6,2)

    with open("medias.txt", "a") as archivo:
        archivo.write(str(media) + " " + nombreAlumno + "\n")

def proceso3():
    max = 0
    alumnoMax = ""
    with open("medias.txt", "r") as archivo:
        for linea in archivo.readlines():
            datos = linea.split(" ")
            nota = float(datos[0])
            alumno = datos[1]
            if nota > max:
                max = nota
                alumnoMax = alumno
    print("Nota máxima", max, alumnoMax)

if __name__ == "__main__":
    lista = []

    for i in range(1,11):
        p1 = Process(target=proceso1, args=(f"alumno{i}.txt",))
        p1.start()
        lista.append(p1)

    for proceso in lista:
        proceso.join()

    lista = []
    for i in range(1,11):
        p2 = Process(target=proceso2, args=(f"alumno{i}.txt", f"alumno{i}"))
        p2.start()
        lista.append(p2)

    for proceso in lista:
        proceso.join()
    
    p3 = Process(target=proceso3)
    p3.start()
    

    p3.join()