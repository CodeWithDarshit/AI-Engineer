
n = int(input("check number perfect or not"))
sum = 0
for i in range(1, n):

  if n%i==0:
    sum = sum+i
    
    if sum == n:
      print("your number is right")
    else:
      print("not ")