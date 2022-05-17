class Number :
    def __init__(self, num) :
        self.num = num;
    
    def cube(self) -> int :
        return self.num * self.num * self.num;
    
    def square(self) -> int :
        return self.num * self.num;
    

num = Number(100);

print(num.square());
print(num.cube());