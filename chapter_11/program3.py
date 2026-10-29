# create class student tha takes 3 marks and has a method average().

class student:
           
    def _init_(self,name , listofMarks):

     self.name= name
     self.listofmarks=listofMarks
    
    def average(self):
     sum=0
     for eachValue in self.listofMarks:
      sum=sum+ eachValue

      average=sum/3
      print("average is:",average)


student1=student("aditya",[67,89,75])
student1.average()