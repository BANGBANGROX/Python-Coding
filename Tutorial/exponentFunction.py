def raiseToPower(a, b) -> int : 
    res = 1;

    for i in range(b) : 
        res *= a;

    return res;

print(raiseToPower(2, 5));    