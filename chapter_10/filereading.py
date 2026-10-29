# #with keyword


# file=open("hello.txt", 'r')
# data=file.read()

# file.close()

# with open("hello.txt","r") as f:
#   data=f.read()
#   print("file data",data)




with open("newfile.txt", "r")as f:
  # line=f.read()
  # line2= f.read()
  # line3=f.read()
  # data=f.read()
  # print("line 1",line)
  # print("line 2",line2)
  # print("line 3",line3)
  # print("file is  data", data)

  readLineMethods =f.readlines()
  print(readLineMethods)