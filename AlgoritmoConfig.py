#programa para ingresar un archivo de configuración .txt

def leer_texto():
    print('ingrese el nombre del archivo de configuracion')
    a = input()
    archivo=(a+'.txt')

    with open(archivo,'r') as documento:
        cont = documento.readline()
        palabras = cont.split()
        lista = []
        for palabra in palabras:
            lista.append(palabra)
            
        factor1 = lista[3]
        factor2 = lista[5]
        bits = lista[1]

    return bits, factor1, factor2
 
bits, factor1, factor2 = leer_texto()

print("cantidad de bits: ", bits)
print("el factor 1 es: ",  factor1)
print("el factor 2 es: ", factor2)
