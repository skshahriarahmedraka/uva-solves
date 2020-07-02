def main():
    k=1
    for _ in [0]*int(input()):
        c,f=[float(i) for i in input().split()]
        f1=((9*c)/5)+32
        f=f+f1
        c=float((f-32)*5/9)
        print(f"Case {k}: {c:.2f}")
        k+=1



if __name__=="__main__":
    main()