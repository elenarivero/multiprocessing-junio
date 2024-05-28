from multiprocessing import Pool

def suma(num1, num2):
    return num1+num2

if __name__ == '__main__':
    with Pool(processes = 3) as pool:
        numeros = [(1,4),(5,8),(3,9)]

        resultados = pool.starmap(suma, numeros)

    print("Resultados: ", resultados)