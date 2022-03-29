banks_list=["kotak","HDFC","RBI","SBI","bank of baroda"]
f1=open("list.txt","w")
i=0
while i<len(banks_list):
    f1.write(banks_list[i])
    f1.write("/n")
    i=i+1
    print(banks_list)