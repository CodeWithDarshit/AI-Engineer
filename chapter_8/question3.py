l = [12,45,6,5,4,4,3,30]

for i in range(len(l)):
  largest =l[0]
  index = 0
  print(l[i])
  if l[i]>largest:
    largest = l[i]
    index=i

    print(f"your largest number is {largest} at index {index}")