a = float(input("Enter a number... "));
b = float(input("Enter another number... "));
op = input("Enter a valid operation... ");

if (op == '+') :
    print(a + b);
elif (op == '-') :
    print(a - b);
elif (op == '*') :
    print(a * b);
elif (op == '/') :
    print(a / b);
elif (op == '^') :
    print(a ** b);
else :
    print("Invalid operation!!!");