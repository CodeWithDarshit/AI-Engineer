from pathlib import Path

def readfilefolder():
  path=Path('')
  items = list(path.rglob('*'))
  for i, items in enumerate(items):
    print(f"{i+1} : {items}")


def creatfile():
  try:
    readfilefolder()
    name = input("please tell your name:-")
    p=Path(name)
    if not p.exists():
     with open(p, "W")as fs:
       data = input("what you want to wirte the file:-")
     fs.write(data)

     print(F"FILE CREATED RIGHT")
    else:
     print("this file right exists")
 
  except Exception as err:
   print(f"an error occured as{err}")

   def readfile():
     readfilefolder()
     name = input("which file want to read")





  
  print("press 1 for creating a file")
  print("press 2 for reading a file")  
  print("press 3 for uppdating a file")
  print("press 4 for deletion a file")

  check = int(input("please tell your response:-"))

  if check ==1:
    creatfile()

  if check ==2 :
    readfilefolder()