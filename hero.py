a=int(input("enter a"));
b=int(input("enter b"));
c=int(input("enter c"));
d=int(input("enter d"));
e=int(input("enter e"));
file1=open("file.txt","w")
if(a>0 and b>0 and c>0 and d>0 and e>0):
    print(a+b+c+d+e)
    total=a+b+c+d+e
    file1.write("total: %d"%total)
else:
    print("should provide positive number")
    file1.write("should provide positive number")
file1.close()