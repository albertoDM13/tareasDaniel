def isEntero(n):
  # Funcion para saber si un numero es entero
    try:
        int(n)
        return n 
    except ValueError:
        print("El Numero "+n+" No es un Entero, Adios!!!")
        return exit(1)

def isNum(cand):       
   # Funcion para saber si la cadena es un numero
     if cand.isdigit():
         print('Como Puedes Estar, ',cand)
     else:
         return cand



def sumatoriaNM():
    print(' ')
    print('HACER LA SUMATORIA DE n NUMERO A m')
    n = isEntero(input("introduce un numero entero, "))
    m = isEntero(input("introduce otro numero entero, "))
    a = 0
    for i in range(n, m):
        a = a + i
        print( a,i )
    

def numeroPar():
    mod = float(2)
    print('SABER SI UN NUMERO ES PAR O NO')
    n = float(isEntero(input('Introduce un Numero Entero, ')))
    if n%mod == 0:
        print('El numero ',int(n),' es PAR')
    else:
        print('El numero ',int(n),' es IMPAR')


def helloWord():
    # arrays de estados de animos
    negation = ['mal', 'malo', 'pesimo']
    confirmation = ['bien', 'excelente']

    # Se pide la respuesta y se tranforma en minusculas
    cand = isNum(input('Hola Buenos Dias!!!\n Como esta Usted?\n')).lower()
    # Dividimos la cadena en un array por serparacion de espacios
    candArray = cand.split(' ')
    
    # Comprobamos el estado de animo
    for j in candArray:
        for i in negation: 
            if j == i:
                print('Lastima que usted se sienta, ',i)
                exit(1)
            else:
                for b in confirmation:
                    if j == b:
                        print('Me alegra que usted este, ',b)
                        exit(1)
                    

def bucles():
    for i in range(0, 5):
        for j in range(0, 3):
            print(i, j)
            '''
             Salida 0 0
                    0 1
                    0 2
                    1 0
                    1 1
                    1 2
                    2 0
                    2 1
                    2 2
                    3 0
                    3 1
                    3 2
                    4 0
                    4 1
                    4 2 '''
    print('  .')
    for i in range(0, 5):
        for j in range(i, 5):
            print(i, j)
            '''
             Salida 0 0
                    0 1
                    0 2
                    0 3
                    0 4
                    1 1
                    1 2
                    1 3
                    1 4
                    2 2
                    2 3
                    2 4
                    3 3
                    3 4
                    4 4 '''
    print('  .')
    for i in range(0, 5):
        for j in range(0, i):
            print(i, j)
            '''
             Salida 1 0
                    2 0
                    2 1
                    3 0
                    3 1
                    3 2
                    4 0
                    4 1
                    4 2
                    4 3'''


# Descomentar La llamada a la Funcion que quieras utilizar
# pero solo tener una funcion a la vez.
#

'''sumatoriaNM()'''
'''queResultado()'''
'''numeroPar()'''
'''helloWord()'''
'''bucles()'''