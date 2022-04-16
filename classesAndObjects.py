class Student :
    def __init__(self, name, regNum) : # constructor
          self.name = name;
          self.regNum = regNum;

student1 = Student("Lakshya Bang","2019UGCS082");

print(student1.name + " " + student1.regNum);