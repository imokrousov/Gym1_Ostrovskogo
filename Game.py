N = 223 #Граница выхода
def End(x,y):
    if x+y>= N: #Зависит от задачи
        return  True
    else:
        return False

def neg_max(V):
    for i in range(len(V)-1,-1,-1):
        if (V[i]<0): return  V[i]


def h1(x) :
    return x+1 # Зависит от задачи
def h2(x):
    return  x*2 # Зависит от задачи
#Может быть еще варианты ходов def h3(x)

def FillGame ():
    G = []
    for i in range(N+1) : G.append([0]*(N+1)) # Генерация таблицы размера N+1 на N+1 из нулей
    for i in range (N,0,-1):
        for j in range (N,0,-1):
            if End(i,j): continue # Условие отсекает случаи, когда игры нет
            P = [End(h1(i),j), End(h2(i),j),End(i,h1(j)),End(i,h2(j))]
            for x in P:
                if x:
                    G[i][j]=1
            if G[i][j] == 1 :continue # Условие отсекает случаи, когда первый игрок выйграл 1 ходом
            # Игра не заврешиться за 1 ход
            V = [G[h1(i)][j], G[h2(i)][j],G[i][h1(j)],G[i][h2(j)]] #Если больше вариантов ходов, то все добавит в список
            V.sort()
            if V[0]< 0 : #У первого есть победных ход
                G[i][j] = 1-neg_max(V)
            else: # Все ходы у текущего игрока плохие
                G[i][j] = -V[3]  #Если у вас больше вариантов ходов, то тут нужно брать последнюю V
    return G

G = FillGame()
for i in range(1,N+1):
    if (G[17][i] == 2) :
        print(i)
print("--------------------------")
for i in range(1,N+1):
    if (G[17][i] == -2) :
        print(i)
