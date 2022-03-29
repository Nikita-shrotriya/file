f=open("question3.txt","r")
c=f.readlines()
for i in c:
    if "delhi" in i:
        f1=open("delhi.txt","a")
        f1.write(i)
        print(f1)
    elif "shimla" in i:
        f2=open("shimla.txt","a")
        f2.write(i)
        print(f2)
    else:
        f3=open("others.txt","a")
        f3.write(i)
        print(f3)        

