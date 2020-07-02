def sumdigi(n):
    x=0
    while n:
        x=x+n%10
def main():
    for _ in [0]*int(input()):
        s=[(i) for i in input().split(" ")]
        x=0
        y=0
        #print(s)
        for i in range(4):
            if int(s[i][0]) <5:
                x+=(int(s[i][0])*2)
            if int(s[i][0]) ==5:
                x+=1
            if int(s[i][0]) ==6:
                x+=3
            if int(s[i][0]) ==7:
                x+=5
            if (int(s[i][0])) ==8:
                x+=7
            if int(s[i][0]) ==9:
                x+=9
            if int(s[i][2]) <5:
                x+=(int(s[i][2])*2)
            if int(s[i][2]) ==5:
                x+=1
            if int(s[i][2]) ==6:
                x+=3
            if int(s[i][2]) ==7:
                x+=5
            if int(s[i][2]) ==8:
                x+=7
            if int(s[i][2]) ==9:
                x+=9

            y+=int(s[i][1])
            y+=int(s[i][3])

        if (x+y)%10!=0:
            print("Invalid")
        else:
            print("Valid")


        





if __name__=="__main__":
    main()