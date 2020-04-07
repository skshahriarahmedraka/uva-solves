def main():
    t=int(input())
    for i in range(t):
        x=input()
        n=int(input())
        m=int(input())
        
        for j in range(m):
            
            
            for k in range(1,n+1):
                l=1
                while l<=k:
                    print(k,end="")
                    l+=1
                print()
            
            for k in range(n-1,0,-1):
                l=1
                while l<=k:
                    print(k,end="")
                    l+=1
                
                print()
            
            if i==(t-1) and j==(m-1):
                return 
            print()
        

if __name__=="__main__":
    main()