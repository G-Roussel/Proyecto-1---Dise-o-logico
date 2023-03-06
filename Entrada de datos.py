def Entrada_Datos(bits,num1,num2):
    bits = int(input("Digite la cantidad de bits: "))
    num1 = input("Digite el valor 1: ")
    num2 = input("Digite el valor 2: ")
    
    if num1[0] == 'b':
        largo_numero1 = len(num1)
        num1_nuevo = int(num1[1:largo_numero1])
        num1_bin = format(num1_nuevo,"b")
        num1_compara = str(num1_bin)
        if len(num1_compara) > bits:
            print("El numero 1 que escogio no se puede representar con esta cantidad de bits")
        elif num2[0] == 'b':
            largo_numero2 = len(num2)
            num2_nuevo = int(num2[1:largo_numero2])
            num2_bin = format(num2_nuevo,"b")
            num2_compara = str(num2_bin)
            if len(num2_compara) > bits:
                print("El numero 2 que escogio no se puede representar con esta cantidad de bits")
            else:
                print("Los 2 numeros pueden multiplicarse")
        
        print (num1_nuevo)
        print(num1_bin)
    elif num1[0] == 'h':
        print("El numero es hexadecimal")
    else:
        print("El numero es decimal")
    


Entrada_Datos(2,1,8)
