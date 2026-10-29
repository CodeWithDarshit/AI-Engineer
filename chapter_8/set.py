# a={1,2,3,4,5,6,7}

# print(a)

# print(hash(12))

# a = 12
# b = hash("hello")
# print(b)

# c = hash((1,2,3,4,5))

# print(c)

# a = {1,2,8,7,3,4,5}

# for i in a:
#   print(i)

a = {1,2,3,4,5}
b = {2,4,5,6,7}

# s = a.union(b)
# s=a.intersection(b)
# s=b.difference(a)
# s=b-a

b -=a

print(b)
