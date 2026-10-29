# a=12
# if a ==12:
#   print("hello")


a = int(input("number is"))
try:
 print(10/a)

except Exception as err:
 print(f"sorry {err}")

else:
 print("good not exception")

finally:
 print("i will run no matter what") 

print("ok is ok ")