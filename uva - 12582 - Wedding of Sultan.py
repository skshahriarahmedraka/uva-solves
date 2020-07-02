def main():
    t=int(input())
    for i in range(t):
        dic={}
        s=input()
        li=list(s)
        #print(li)
        for j in range(len(s)):
            dic[s[j]]=0
        slen=len(s)
        j=0
        while j<slen-1:
            #print(f" {li[j]}  {li[j+1]}")
            #print(li)
            if li[j]!=li[j+1]:
                
                dic[li[j]]=dic[li[j]]+1
                dic[li[j+1]]=dic[li[j+1]]+1
                j+=1
                
            elif li[j]==li[j+1]:
                
                del li[j]
                del li[j]
                j-=1
                
                
            slen=len(li)
            

        print(f"Case {i+1}")
        for i in dict(sorted(dic.items(),key =lambda item:item[0])):
            print(f"{i} = {dic[i]}")






if __name__=="__main__":
    main()