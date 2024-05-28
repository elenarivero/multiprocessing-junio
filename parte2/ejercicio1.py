from multiprocessing import Pool


def cuentaVocal(vocal):
    count = 0
    with open("parte2/texto.txt") as archivo:
        for letra in archivo.read():
            if letra == vocal:
                count+=1

    return count

if __name__ == "__main__":
    with Pool(processes=5) as pool:
        vocales = ["a", "e", "i", "o", "u"]

        resultados = pool.starmap(cuentaVocal, vocales)
    
    print(resultados)