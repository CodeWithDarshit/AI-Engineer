file= open("certificate.txt", 'r')
dataoffile=file.read()


dataoffile=dataoffile.lower()

if "live" in dataoffile:
  print("yes live word is present in tha file")

else:
  print("no")