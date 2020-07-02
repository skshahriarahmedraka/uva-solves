def main():
    for _ in [0]*int(input()):
        s1=input()
        s2=input()
        li=["a","e","i","o","u"]
        if len(s1)!=len(s2):
            print("No")
        else:
            b=True
            for i in range(len(s2)):
                if (s1[i] in li )and (s2[i] not in li):
                    b=False
                    break
                if ( s1[i]!=s2[i] ):
                    if s1[i] not in li:
                        b=False
                        break

            if b:
                print("Yes")
            else:
                print("No")






if __name__=="__main__":
    main()
