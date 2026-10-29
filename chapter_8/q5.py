a = [12,13,14,15]

for i in range(len(a)):
  if a[i] < a[i+1]:
    continue

  else:
    print("list is not sorted")
    break

else:
  print("sorted is list")