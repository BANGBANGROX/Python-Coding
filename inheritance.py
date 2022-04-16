class Parent :
    def __init__(self, a) :
        self.a = a;
    
    def printContents(self) :
        print(self.a);

class Child(Parent) :
    def increment(self) :
        self.a += 1;
    
child = Child(10);

child.printContents();
child.increment();
child.printContents();