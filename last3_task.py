def solve25():
    for x in range (0,235):
        for y in range(0, 679):
            S = "1"+str(x)+"5"+str(y)+"9"
            f = False
            for i in range(len (S)-1):
                if S[i]>=S[i+1]:
                    f = True
                    break
            if f : continue
            a = int(S)
            if a<1000000000 and a%21 == 0 :
                print(a)
    for x in range(0, 235):
        S = "1" + str(x) + "5" + "9"
        f = False
        for i in range(len(S) - 1):
            if S[i] >= S[i + 1]:
                f = True
                break
        if f: continue
        a = int(S)
        if a < 1000000000 and a % 21 == 0:
            print(a)
    for y in range(0, 679):
        S = "1"  + "5" +str(y) +"9"
        f = False
        for i in range(len(S) - 1):
            if S[i] >= S[i + 1]:
                f = True
                break
        if f: continue
        a = int(S)
        if a < 1000000000 and a % 21 == 0:
            print(a)

def solve26():
    M = []
    for i in range(10001):
        M.append([])
    F = open("26.txt","r")
    N = int(F.readline())
    for i in range(N):
        x,y = map(int, F.readline().split())
        M[x].append(y)
    for i in range(N):
        M[i].sort()
    sum = 0
    max_polosa = -1
    max_dosadka = -1
    for i in range(N):
        cur = 0
        for j in range(len(M[i])-1):
            cur += (M[i][j+1] - M[i][j]-1)//2
            sum+= (M[i][j+1] - M[i][j]-1)//2
        if cur>max_dosadka:
            max_polosa = i
            max_dosadka = cur
    print(sum, max_polosa, max_dosadka)
    print(M[4902])

def solve27():
    F = open ("27-A.txt", "r")
    N,R = map(int, F.readline().split())
    D = []
    for i in range(N):
        D.append(int(F.readline()))
    D = D*3
    G = [0]*N
    for i in range (N):
        for j in range (N//2):
            G[i]+=j*j*R*R*D[N+i+j] + j*j*R*R*D[N+i-j]
        G[i] +=(N//2)*(N//2)*R*R*D[N+i+(N//2)]
    print(min(G))
solve27()
