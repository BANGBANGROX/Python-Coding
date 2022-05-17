data = open("randomText.txt", "r");

print(data.readable());
print(data.readlines());
print(data.read());

data.close();