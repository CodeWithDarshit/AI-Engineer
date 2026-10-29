#read only the first line of bio.txt

with open("bio.txt", 'r') as f:
  line1 = f.readline()
  print("line 1", line1)