def F (s):
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01','2302',1)
        s = s.replace('02', '10', 1)
        s = s.replace('03', '201', 1)
    return s

def solve12():
    for x in range (0,101):
        for y in range(0, 101):
            for z in range(0, 101):
                s = '0'+'1'*x+'2'*y+'3'*z
                w = F(s)
                if (w.count('1') == 51 and
                w.count('2')==29 and w.count('3') ==23):
                    print(x,y,z)


def solve8():
    counter = 0
    for c1 in ['К','У','С','А','Т']:
        for c2 in ['К', 'У', 'С', 'А', 'Т', 'Ь']:
            for c3 in ['К', 'У', 'С', 'А', 'Т', 'Ь']:
                for c4 in ['К', 'У', 'С', 'А', 'Т', 'Ь']:
                    for c5 in ['К', 'У', 'С', 'А', 'Т', 'Ь']:
                        S = c1+c2+c3+c4+c5
                        if 'СУК' in S : continue
                        if S.count('К') >1 : continue
                        if S.count('У') > 1: continue
                        if S.count('С') > 1: continue
                        if S.count('А') > 1: continue
                        if S.count('Т') > 1: continue
                        if S.count('Ь') > 1: continue
                        counter+=1
    print(counter)



def solve26():
    F = open ("26-49.txt", "r")
    counter = 0
    N = int(F.readline())
    L = []
    for i in range(N):
        L.append(int(F.readline()))
    L.sort()
    med = L[2499] # больше med ровно 2500 чисел
    for i in range(N):
        for j in range(i+1,N):
            sum = L[i]+L[j]
            if sum%2 == 0 and sum//2 <= med :
                counter +=1
    print(counter)
