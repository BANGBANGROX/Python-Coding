# Same as unordered_map in C++ or Hashmap in Java

monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
};

print(monthConversions["Jan"]);
print(monthConversions["Nov"]);
print(monthConversions.get("Dec"));
print(monthConversions.get("Luv","Not a valid key"));