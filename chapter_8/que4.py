l = [12,23,45,56,78]

largest = l[0]
sec = l[0]

for i in l:
  if i > largest:
    sec = largest
    largest = i
  elif i>sec:
    sec=i

    print(sec,largest)
