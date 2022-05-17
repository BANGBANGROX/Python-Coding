friends = ["John", "Jonas", "Derek", "James", "Stuart", "Joe", "John"];
luckyNumbers = [1, 2, 45, 69, 89];

#friends.extend(luckyNumbers); # friends = friends + luckyNumbers
friends.append("Julia"); # push_back in C++ or add in Java
friends.insert(0, "Jane"); # simple 
friends.remove("Derek"); 
#friends.clear();
friends.pop();
friends.sort();

print(friends);
print(friends.index("Jonas"));
print(friends.count("John"));

luckyNumbers.reverse();

print(luckyNumbers);

friends2 = friends.copy();
print(friends2);