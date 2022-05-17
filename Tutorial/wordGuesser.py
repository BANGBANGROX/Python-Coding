secretWord = "giraffe";
guess = "";
guesses = 0;
guessLimit = 3;

while (guess != secretWord and guesses < guessLimit) :
    guess = input("Enter an animal name... ");
    guesses += 1;

if (guess == secretWord) : print("Success!");
else : print("Out of guesses, loss :(");
