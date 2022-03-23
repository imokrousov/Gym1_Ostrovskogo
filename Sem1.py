def solve2():
    for x in [False, True]:
        for y in [False, True]:
            for z in [False, True]:
                for w in [False, True]:
                    F = (not x or y and not z) or w # Здесь формула
                    if F == False: # Что ищем в таблице
                        print(x,y,z,w)

def solve6():
    for x in range(-10000,10000):
        s = x
        n = 1
        while n < 21:
            s = s - 1
            n = n + 2
        if s>600 :
            print(x)
            break



def solve12():
    s ="8"*9+ "5"*12
    #ПОКА нашлось (555) ИЛИ нашлось (888)
    while "555" in s or "888" in s:
        #ПОКА нашлось (555)
        while "555" in s:
            #заменить (555, 8)
            s = s.replace("555","8",1)
        #ПОКА нашлось (888)
        while "888" in s:
            #заменить(888, 5)
            s = s.replace("888","5",1)
    print(s)

def solve14():
    x = 3*4**48+2*2**23+4**20+3*4**5+2*4**4+1 # Поставить число
    s=""
    counter = 0
    while x>0:
        if x%16 == 0 : # Что считать?
            counter +=1
        s = str(x%16)  + s # Это не обязательно
        x //= 16 # x= x//16
    print(s  , counter)

solve14()
