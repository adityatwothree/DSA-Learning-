L=0

def TheGreatAnswer(s) :
    if len(s) == 1 :
          
        return s[0] 
    else :
        bottleneck = min(s)
        ind = s.index(bottleneck)
        for mem in range(len(s)) :
            if s[mem] == bottleneck :
                ind = mem  
        L = bottleneck * len(s)
        s = [(x- bottleneck) for x in s ]

        return TheGreatAnswer(s[:ind]) + L
        


T= int(input())
for _ in range(T) :
    N= int(input())
    s = input().strip().split()
    s= [int(x) for x in s]
    print(TheGreatAnswer(s))