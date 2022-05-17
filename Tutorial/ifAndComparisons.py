def maxNum(a, b, c) -> int : 
    if (a > b) :
        if (a > c) : return a;
        return c;
    if (b > c) : return b;
    return c;

result = maxNum(11, -3, -3);

print(result);