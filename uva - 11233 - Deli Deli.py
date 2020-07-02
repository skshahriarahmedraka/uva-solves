def main():
    n,m=[int(i) for i in input().split(" ")]
    dic={}
    li=["a","e","i","o","u"]
    li2=["o","s","x"]
    li3=["ch","sh"]
    for i in range(n):
        s1,s2=[ j for j in input().split(" ")]
        dic[s1]=s2
    for i in range(m):
        s=input()
        if s in dic:
            print(dic[s])
        elif (s[-2] not in li) and s[-1]=="y":
            print(s[:-1]+"ies")
        elif s[-1] in li2:
            print(s+"es") 
        elif s[-2]+s[-1] in li3:
            print(s+"es")
        else:
            print(s+"s")

if __name__=="__main__":
    main()