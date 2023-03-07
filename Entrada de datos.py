def Hexadecimal_Decimal(digito):
    digitos = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in range(len(digitos)):
        if digito == digitos[i]:
            return i

def HexToDeci(hexnum):
    decNum = 0
    potencia = 0
    for digito in range(len(hexnum),0,-1):
        decNum = decNum + 16 ** potencia * Hexadecimal_Decimal(hexnum[digito-1])
        potencia = potencia + 1
    return decNum

def Deci_Binario(hexnum):
    x = HexToDeci(hexnum)
    x = format(x,"b")
    return x      

def Entrada_Datos(bits,num1,num2):
    bits = int(input("Digite la cantidad de bits: "))
    num1 = input("Digite el valor 1: ")
    num2 = input("Digite el valor 2: ")
#caso en el que num 1 es decimal    
    if num1[0] == 'd':
        largo_numero1 = len(num1)
        num1_nuevo = int(num1[1:largo_numero1])
        num1_bin = format(num1_nuevo,"b")
        num1_compara = str(num1_bin)
        if len(num1_compara) > bits:
            print("El numero 1 que escogio no se puede representar con esta cantidad de bits")
        elif num2[0] == 'd':
            largo_numero2 = len(num2)
            num2_nuevo = int(num2[1:largo_numero2])
            num2_bin = format(num2_nuevo,"b")
            num2_compara = str(num2_bin)
            if len(num2_compara) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(num1_bin)
                print(num2_bin)
                
        elif num2[0] == 'h':
            largo_numero2 = len(num2)
            num2_nuevo = str(num2[1:largo_numero2])
            Deci_Binario(num2_nuevo)
            num2_compara = Deci_Binario(num2_nuevo)
            if len(num2_compara) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(num1_bin)
                print(Deci_Binario(num2_nuevo))

        elif num2[0] == 'b':
            largo_numero2 = len(num2)
            num2_nuevo = str(num2[1:largo_numero2])
            if len(num2_nuevo) > bits:
                print("El numero 1 que escogio no se puede representar con esta cantidad de bits")
            else:
                print(num1_bin)
                print(num2_nuevo)
        else:
            largo_numero2 = len(num2)
            num2_nuevo = int(num2[0:largo_numero2])
            num2_bin = format(num2_nuevo,"b")
            num2_compara = str(num2_bin)
            if len(num2_compara) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(num1_bin)
                print(num2_bin)
                
#caso en el que num 1 es hexadecimal
    elif num1[0] == 'h':
        largo_numero1 = len(num1)
        num1_nuevo = str(num1[1:largo_numero1])
        Deci_Binario(num1_nuevo)
        num1_compara = Deci_Binario(num1_nuevo)
        if len(num1_compara) > bits:
            print("El numero 1 que escogio no se puede representar con esta cantidad de bits")
        elif num2[0] == 'h':
            largo_numero2 = len(num2)
            num2_nuevo = str(num2[1:largo_numero2])
            Deci_Binario(num2_nuevo)
            num2_compara = Deci_Binario(num2_nuevo)
            if len(num2_compara) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(Deci_Binario(num1_nuevo))
                print(Deci_Binario(num2_nuevo))
        elif num2[0] == 'd':
            largo_numero2 = len(num2)
            num2_nuevo = int(num2[1:largo_numero2])
            num2_bin = format(num2_nuevo,"b")
            num2_compara = str(num2_bin)
            if len(num2_compara) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(Deci_Binario(num1_nuevo))
                print(num2_bin)
        elif num2[0] == 'b':
            largo_numero2 = len(num2)
            num2_nuevo = str(num2[1:largo_numero2])
            if len(num2_nuevo) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(Deci_Binario(num1_nuevo))
                print(num2_nuevo) 
        else:
            largo_numero2 = len(num2)
            num2_nuevo = int(num2[0:largo_numero2])
            num2_bin = format(num2_nuevo,"b")
            num2_compara = str(num2_bin)
            if len(num2_compara) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(Deci_Binario(num1_nuevo))
                print(num2_bin)
                
#caso en el que num 1 es binario
    elif num1[0] == 'b':
        largo_numero1 = len(num1)
        num1_nuevo = str(num1[1:largo_numero1])
        if len(num1_nuevo) > bits:
            print("El numero 1 que escogio no se puede representar con esta cantidad de bits")
        elif num2[0] == 'h':
            largo_numero2 = len(num2)
            num2_nuevo = str(num2[1:largo_numero2])
            Deci_Binario(num2_nuevo)
            num2_compara = Deci_Binario(num2_nuevo)
            if len(num2_compara) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(num1_nuevo)
                print(Deci_Binario(num2_nuevo))
        elif num2[0] == 'd':
            largo_numero2 = len(num2)
            num2_nuevo = int(num2[1:largo_numero2])
            num2_bin = format(num2_nuevo,"b")
            num2_compara = str(num2_bin)
            if len(num2_compara) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(num1_nuevo)
                print(num2_bin)
        elif num2[0] == 'b':
            largo_numero2 = len(num2)
            num2_nuevo = str(num2[1:largo_numero2])
            if len(num2_nuevo) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(num1_nuevo)
                print(num2_nuevo)
        else:
            largo_numero2 = len(num2)
            num2_nuevo = int(num2[0:largo_numero2])
            num2_bin = format(num2_nuevo,"b")
            num2_compara = str(num2_bin)
            if len(num2_compara) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(num1_nuevo)
                print(num2_bin)
            
            
#caso en donde no se pone letra antes del numero                   
    else:
        largo_numero1 = len(num1)
        num1_nuevo = int(num1[0:largo_numero1])
        num1_bin = format(num1_nuevo,"b")
        num1_compara = str(num1_bin)
        if len(num1_compara) > bits:
            print("El numero 1 que escogio no se puede representar con esta cantidad de bits")
        elif num2[0] == 'd':
            largo_numero2 = len(num2)
            num2_nuevo = int(num2[1:largo_numero2])
            num2_bin = format(num2_nuevo,"b")
            num2_compara = str(num2_bin)
            if len(num2_compara) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(num1_bin)
                print(num2_bin)
                
        elif num2[0] == 'h':
            largo_numero2 = len(num2)
            num2_nuevo = str(num2[1:largo_numero2])
            Deci_Binario(num2_nuevo)
            num2_compara = Deci_Binario(num2_nuevo)
            if len(num2_compara) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(num1_bin)
                print(Deci_Binario(num2_nuevo))

        elif num2[0] == 'b':
            largo_numero2 = len(num2)
            num2_nuevo = str(num2[1:largo_numero2])
            if len(num2_nuevo) > bits:
                print("El numero 1 que escogio no se puede representar con esta cantidad de bits")
            else:
                print(num1_bin)
                print(num2_nuevo)
        else:
            largo_numero2 = len(num2)
            num2_nuevo = int(num2[0:largo_numero2])
            num2_bin = format(num2_nuevo,"b")
            num2_compara = str(num2_bin)
            if len(num2_compara) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
                print(num1_bin)
                print(num2_bin)
    


Entrada_Datos(2,1,8)
