class Juego:
    import random

    def __init__(self, n:int=3, jugadores:dict={}, computadoras:list=[]):
        self.n = n
        self.M = [[y*n+1+x for x in range(n)] for y in range(n)]

        self.jugadores = jugadores
        self.computadoras = computadoras

        self.njugadores = len(jugadores)

        for turno in range(n*n):
            jugador = turno%self.njugadores
            if jugador in self.computadoras:
                res = self.JugarComputadoras(jugador)
            else:
                res = self.JugarJugadores(turno, jugador)
            if res:
                print(f"Gano {self.jugadores[turno%self.njugadores]}")
                break
        self.MostrarM()

    def opciones(self):
        opciones = set()
        jugadores = [x for x in self.jugadores.values()]
        for y in range(self.n):
            for k in self.M[y]:
                if not k in jugadores:
                    opciones.add(k)
        return opciones

    def JugarJugadores(self, turno, jugador):
        self.MostrarM()
        eleccion = int(input(f"{self.jugadores[turno%self.njugadores]} > "))
        return self.Turno(jugador, eleccion)

    def JugarComputadoras(self, jugador):
        eleccion = self.random.choice(list(self.opciones()))
        return self.Turno(jugador, eleccion)

    def buscarM(self, k:int):
        for y in range(self.n):
            try:
                return y, self.M[y].index(k)
            except Exception as exp:
                #print(exp)
                pass
        raise ValueError()

    def MostrarM(self):
        print("\n")
        for i in range(self.n):
            print(*self.M[i])
        print("\n")

    def Turno(self, jugador:int, k:int):
        y, x = self.buscarM(k)
        self.M[y][x] = self.jugadores[jugador]
        return self.VerificarFin(y,x)

    def VerificarFin(self,y:int,x:int):
        for j in range(self.n):
            fila=set(self.M[j])
            if len(fila)<=1:
                return True
        for j in range(self.n):
            columna = {self.M[j][i] for i in range(self.n)}
            if len(columna)<=1:
                return True

        diagonal = {self.M[i][i] for i in range(self.n)}
        if len(diagonal)<=1:
                return True
        diagonal = {self.M[i][self.n-i-1] for i in range(self.n)}
        if len(diagonal)<=1:
                return True
        return False



n = 3#int(input("n > "))
jugadores={0:"O",1:"X"}#{x:input(f"Player {x}. ") for x in range(j)}
computadoras=[0,1,2]#[int(input()) for x in range(c)]
for _ in range(10):
  Juego(n, jugadores, computadoras)
