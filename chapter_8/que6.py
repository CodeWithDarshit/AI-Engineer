a = [1,2,3,3,4,5,5,5,6,7,7,7,7,8,8]

d={}
for i in a:
  if i in d.keys():
    d[i]+=1
  else:
    d[i]=1

    print(d)
  