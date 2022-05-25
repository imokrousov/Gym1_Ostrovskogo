def solve8():
    L = ['Г','Е','К','Э','0','2','3']
    n = 1
    s = ""
    for x in L:
        for y in L:
            for z in L:
                for w in L:
                    s = x+y+z+w
                    if s[0] in ['0','2','3'] and s[0]!=s[1] and s[1]!= s[2] and s[2]!= s[3]:
                        print(n,s)
                        return
                    n+=1
def D(x,y):
    return  x%y == 0

def solve15():
    counter = 0
    for A in range(-2000, 2001):
        if A==0: continue
        flag = True
        for x in range (-20000, 20001):
            if (D(A,25) and ( not(D(x,24) and D(x,75)) or D(x,A) )) == False:
                flag = False
        if flag :
            counter +=1
    print(counter)

def check_1_mask (s):
    for i in range(0, len(s) -3 ):
        if s[i] == '0' and s[i+3] == '3':
            return  True
    return  False

def check_2_mask (s):
    if s[-1] == '2' and s[-4] =='4' :
        return True
    return  False

def check_3_mask (s):
    if '1' in s:
        return  True
    return False

def solve25():
    Ans = []
    x = 700011
    while (len(Ans) < 5):
        if not check_1_mask(str(x)):
            if not check_2_mask(str(x)):
                if not check_3_mask(str(x)):
                    Ans.append(x)
        x+=13
    print(Ans)

def solve12():
    for n in range (1,1001):
        for a in range(-100,100):
            for b in range (-100,100):
                if (-1+n*(a-1) - 24 ==0) and (-2+n*(b-2)-12 == 0):
                    print(n)

def Proizv(x):
    ans = 1
    while x>0:
        ans*=x%10
        x//=10
    return  ans

def Sum (x):
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10
    return ans

def solve12a(_from, _to):
    if (_from == _to): return 1
    if (_from < _to or _from == 9): return  0
    return  solve12a(Proizv(_from),_to) + solve12a(Sum(_from),_to)

def solve12b(_from, _to):
    if (_from == _to): return 1
    if (_from > _to '''or _from == НЕЛЬЗЯ''') : return 0
    return solve12b(_from+1,_to) + solve12b(10*_from+1, _to)

print(solve12b(Начало,Обязательно)*solve12b(Обязательно,Конец))
print(solve12b(1,512))

'''

counter = 0
for x in range (8, 2000):
    if (solve12(x,8) > 0):
        print(x)
        counter +=1
print(counter)'''
