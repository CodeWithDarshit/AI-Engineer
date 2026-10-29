import random    #random is librery

num = random.randint(1,10)


tries = 0

while True:
  break
guesss = int(input("please gase your number :"))
if num == guesss:
  tries+=1
  print(f"right numbr is {tries} tries")
  

elif num < guesss:
  print("go little lower")

  tries+=1
  
elif num > guesss:
 print("go little higher")
 tries+=1

else:
    tries+=1
    print("sorry")


 