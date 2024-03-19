def suma( num1, num2):
    return num1+num2


def resta( num1, num2):
    return num1-num2

def multiplicacion( num1, num2):
    return num1*num2

def division( num1, num2):
    
    if num2 == 0:
        return "No se puede dividir entre 0"
    else:
        resultado = round(num1/num2, 3)
        return resultado

def salir():
    return "Hasta luego"
    functs.exit()