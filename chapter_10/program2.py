#print how many lines are present in notes.txt

import os

try:
 with open("notes5.txt",'r') as f:
  listoflines = f.readlines()
  print("output of read lines method", listoflines)
  print("number of lines in file", len(listoflines))

except:
  print("that files not exist") 


  #rename the file

  # os.rename("report1.txt", "darshit.txt")
  # os.remove("darshit.txt")