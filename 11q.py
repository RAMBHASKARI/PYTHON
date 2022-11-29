print("Prime numbers between 1 and 20 are:")
prime =20;
for num in range(prime):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
