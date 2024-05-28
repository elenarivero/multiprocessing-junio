from multiprocessing import Pool

def suma(num1):
    suma = 0
    for i in range(1,num1+1):
        suma += i
    return suma

if __name__ == '__main__':
    with Pool(processes = 3) as pool:
        numeros = [1,4,5,8,3,9]

        resultados = pool.map(suma, numeros)

    print("Resultados: ", resultados)