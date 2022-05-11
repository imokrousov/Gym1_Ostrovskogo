def solve24_1():
    F = open ("24.txt", "r")
    S = F.readline()
    n = len(S)
    max_len = -1
    cur = 1
    for i in range (1,n):
        if (S[i] == 'a' and S[i-1] == 'd') or (S[i] == 'd' and S[i-1] == 'a'): # Условие разрыва подстроки
            max_len = max(max_len,cur)
            cur = 1
        else:
            cur+=1
    max_len = max(max_len,cur)
    print(max_len)

def solve24_2(): #Только при улосвии, что нет подрят условий разрыва
    F = open("24.txt", "r")
    S = F.readline()
    S = S.replace("ad", '#')
    S = S.replace("da", '#')
    MS = S.split('#')
    max_len=-1
    for i in range(0,len(MS)):
        x = len(MS[i])
        if i == 0 or i == len(MS)-1 : x+=1
        else: x+=2
        max_len=max(max_len,x)
    print(max_len)

def solve24_3():
    F = open("24.txt", "r")
    S = F.readlines()
    max_dist = -1
    for i in range (len(S)):
        count_G = 0
        for j in range (len(S[i])-1):
            if S[i][j] =='G': count_G+=1
        if count_G >= 25: continue
        START = [-1]*26
        END = [-1]*26
        for j in range(len(S[i]) - 1):
            c = S[i][j]
            index = ord(c) - ord('A')
            if START[index] == -1:
                START[index] = j
            END[index] = j
        for j in range(26):
            if END[j]==-1:continue
            max_dist = max(max_dist, END[j]-START[j])
    print(max_dist)

def solve24_4():
    F = open("24.txt", "r") # S = open("24.txt","r").readlines()
    S = F.readlines()
    max_dist = -1
    for i in range(len(S)):
        if S[i].count("G")>= 25 : continue
        for c in "ABCDEFGHIKJLMNOPQRSTUVWXYZ":
            max_dist = max(max_dist, S[i].rfind(c) - S[i].find(c))
    print(max_dist)
solve24_4()
