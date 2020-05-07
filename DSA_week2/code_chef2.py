T = int(input())
ans =[]
for _ in range(T):
    N= int(input())
    shots = input().strip()
    shotA = shots[::2]
    shotB =shots[1::2]
    scoreA,scoreB,s1,s2=0,0,0,0
    for i,j in zip(shotA,shotB): 
         if scoreA > scoreB + N -s2 :
             break
         scoreA+=int(i)
         s1+=1 
         if scoreB > scoreA + N -s1 :
             break
         scoreB+=int(j)
         s2+=1
    ans.append(s1+s2) 
for x in ans :
    print(x)  
    # for i in range(len(shots)) :
        
    #     if int(i) %2 ==0 :
    #         s+=1
    #         scoreA += int(shots[i])
            
    #         if scoreA > scoreB + int(((2*N) - s)/2)   :
    #             break
    #     else :
    #         scoreB += int(shots[i])
    #         s+=1
    #         if scoreB >= scoreA + ((2*N) - s)/2 :
    #             break
    # print(s)