# Clase para establecer las conexiones entre 2 nodos
class Conexion:
    def __init__(self):
        self.x = 0 #por defecto no poseen grado de conexion

    def conectar(self, A, B, grado, i):
        self.x = grado #grado de transicion
        self.A = A #estado inicial
        self.B = B #estado final
        self.i = i #transicion
#Clase para definir la estructura del grafo
class Grafo:
    def __init__(self):
        self.nodos = []

    def crear(self, cantidad):
        self.nodos = []
        for i in range(cantidad):
            self.nodos.append(Nodo())
            self.nodos[i].crear(i)
    
    def conectar(self, A , B, grado, i):
        self.nodos[A].conexiones.append( Conexion().conectar(A, B, grado, i))
#Clase para definir la estructura del nodo
class Nodo:
    def __init__(self):
        self.nro = 0
        self.conexiones = []
    def crear(self, nro):
        self.nro = nro
        self.conexiones = [] 
    def conectar(self,A,B,grado,i):
        nuevo = Conexion()
        nuevo.conectar(A,B,grado,i)
        self.conexiones.append(nuevo)


def menu():
    
    cantidad = int(input("Ingrese la cantidad de estados\n"))
    estados = Grafo()
    estados.crear(cantidad)
    print("Ingrese los elementos del diccionario -1 para finalizar diccionario\n")
    dicc = []
    i = 1
    while i == 1 :
        a = input()
        if a!="-1":
            dicc.append(a)
        else :
            break
    cantRelaciones = int(input("Ingrese la cantidad de transiciones\n"))
    for j in range(cantRelaciones):
        A = int(input("Ingrese el estado A (de 0 a n-1)\n"))
        B = int(input("Ingrese el estado B (de 0 a n-1)\n"))
        x = input("Ingrese la letra del diccionario\n")
        grado = float(input("Ingrese el grado entre A y B\n"))

        estados.nodos[A].conectar(A, B, grado , x)

    return estados
        
# funcion recursiva que retorna el grado de x en el lenguaje aceptado por M
def grado_total(A,x, i):
    #definicion de cola de vecinos para cada instancia de la llamada recursiva
    vecinos = []
    # inidicar si es posible pasar de un estado a otro
    tieneConexion = 0
    #ver todas las transiciones posibles de la cadena x
    #ultima variable ya no tiene transicion
    if i<len(x):
        #Z es una transicion entre dos estados
        for Z in grafo.nodos[A].conexiones : 
            #si el estado A tiene una transicion posible
            if Z.i == x[i]:
                grado = Z.x #de A a B
                grado_2 = (grado_total(Z.B, x , i+1))
                #en caso de que el estado B (siguiente instancia de llamada recursiva) no tenga transicion
                if grado_2 != None:
                    grado = min(grado, grado_2)
                tieneConexion = 1
                #se agrega el menor grado
                vecinos.append(grado)

    if tieneConexion == 0:
        return None
    #en caso de no deterministico se elige el máximo posible
    maxi = max(vecinos)
    return maxi


    
grafo = menu()
x = input("Ingrese x\n")
print(grado_total(0,x,0))

