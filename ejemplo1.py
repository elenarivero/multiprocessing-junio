from multiprocessing import Process

def suma(num1):
    suma = 0
    for i in range(1,num1+1):
        suma += i
    print(suma)


if __name__ == '__main__':
    numero1 = int(input('Introduzca un número: '))
    numero2 = int(input('Introduzca otro número: '))

    p1 = Process(target=suma, args=(numero1,))
    p1.start()

    p1.join()