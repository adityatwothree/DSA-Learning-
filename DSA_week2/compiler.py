class stack :
    def __init__(self):
    
        items =[]

    def push(self,element) :
        self.items.append(element)
        

    def pop(self) :
        if len(self.items) == 0 :
            print("stack underflow")
            return
        return self.items.pop()
    def is_empty(self) :
        if len(self.items) ==0 :
            return True 
        return False

def longest_prefix(s) :
    # prefix=0
    # count=0
    # for each in stri :
    #     if each == "<" :
    #         count+=1
    #         s.push(each)
    #     else :
    #         if s.pop() != ">" :
    #             count+=1
    #             if count > prefix :
    #                 prefix = count
    countA,countB =0,0

    for i in range(len(s)) :
        if s[i] == "<":
            countA+=1
        else:
            countB+=1
        if countB > countA :
            break
    print(i)
    return 0



stri = input().strip()
longest_prefix(stri)