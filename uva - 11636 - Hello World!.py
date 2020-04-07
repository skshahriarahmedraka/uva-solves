def main():
    i=1
    while True:
        n=int(input())
        if n <0:
            return
        x=1
        count=0
        while True:
            if x>=n:
                break
            
            x+=(x)
            #print(x)
            count+=1
        print(f"Case {i}: {count}")
        i+=1


if __name__=="__main__":
    main()