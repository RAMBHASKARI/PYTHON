n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


#n = int(input("Enter the no.of rows you want to print : "))  
#for i in range(0,n):
#   for j in range(0,i+1):
#      print("*",end="")
#   print()

n=5;
for i in range(n):
    for j in range(i):
        print('*',end="")
    print('')