# Giraffe language
# vowels -> g
# dog -> dgg
# cat -> cgt

def translate(phrase) :
    translation = "";
    for letter in phrase :
        if (letter in "AEIOUaeiou") :
            if (letter.isupper()) : translation += 'G';
            else : translation += 'g';
        else :
            translation += letter;
    
    return translation;

phrase = input("Enter an english phrase... ");

print("Translated phrase = " + translate(phrase));