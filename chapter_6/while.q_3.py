a = int(input("tell yoyr number:"))
rev = 0
copy = a

while a>0:
  rev = rev *10 + a%10
  a=a//10

  if copy == rev:
    print("palindrome num")

  else:
    print("not number")