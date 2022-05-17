isMale = False;
isTall = True;

if (isMale or isTall) :
    print("You are tall or male or both");
else :
    print("You are neither male nor tall");

if (isMale and isTall) :
    print("You are a tall male");
elif (isMale and not isTall) :
    print("You are a short male");
elif (not isMale and isTall) : 
    print("You are not male but are tall");        
else : 
    print("You are not a male and are not tall"); 

    