a = "jhsajfhdjfdgfgfjg$3^"
char = 0
dig = 0
spchr = 0

for i in a:
  if i.isdigit():
    dig+=1
  elif i.isalpha():
   char +=1
else:
  spchr+=1

  print(f"your digits are {dig}\n your alpha are {char}\n your spcecial {spchr}")


  # print(dir(str))