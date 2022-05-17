name = "Lakshya Bang";
birthYear = 2001;
age = 20;

def power(a, b) -> int : 
    res = 1;

    while (b > 0) : 
        if (b % 2 == 1) :
            res *= a;
            b -= 1;
        a *= a;
        b /= 2;
    
    return res;

def printArr(nums) :
    for num in nums :
        print(num);