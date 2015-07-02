class QUE1():
    def __init__(self, height , count):
        self.H = height
        self.C = count
    
    def __eq__(self , other):
        return self.__dict__ == other.__dict__

def GetOrder(people):
    people.sort(key= lambda p : p.H)
    people1 = list(people)
    for p in people:
        ii = people1.index(p)
        next = None
        for index in range(ii + 1 , len(people1)):
            if people1[index].H > people1[ii].H:
                next = people1[index]
                break
        if next is None:
           continue
        jj = people1.index(next)
        c = p.C
        if c == 0:
            prev = ii -1
            while prev >= 0 and people1[prev].H > people1[ii].H:
                prev = prev - 1
            prev = prev + 1
            people1[ii] , people1[prev] = people1[prev], people1[ii]
            continue
        while c > 0:
            people1[ii] , people1[jj] = people1[jj] , people1[ii]
            ii = ii + 1
            jj = jj + 1
            c = c - 1
    return people1

T = int(raw_input())
while T > 0:
    n = raw_input()
    heights = raw_input().split()
    counts = raw_input().split()
    people = []
    for h,c in zip(heights , counts):
        people.append(QUE1(int(h) , int(c)))
    for p in GetOrder(people):
        print(p.H),
    T = T - 1
