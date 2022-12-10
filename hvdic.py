cars={}
n=int(input("enter number of features"))
for i in range(n):
    key=input("key:")
    value=input("value:")
    cars[key]=value
print(cars)
with open("heheheh.txt","w") as data1:
    data1.write("cars \n")
    for keys,values in cars.items():
        data1.write('%s:%s\n' % (keys,values))
    data1.close()