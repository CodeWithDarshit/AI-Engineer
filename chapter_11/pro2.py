class student:
  schoolname ="abc school"

  def __init__(self,name,course):
    # print("whnwhere a new object is created i am called automaticly")
    # print(self)
    self.name=name
    self.course=course
    print(self.name)
    print(self.course)


student1=student("darshit", "btech") #init method will be called
print("student name :-", student1.name)
print("student name :-", student1.course)


print(student1.schoolname)
print("student 1 ", student1.name)
print("student 2 ", student1.course)

studnet2=student("dev","bca")
print(studnet2)