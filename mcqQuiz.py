class Question :
    def __init__(self, promt, answer) :
        self.promt = promt;
        self.answer = answer;

questionsData = [
    "1.) Who won the ICC Men's WC 2015\na.) India\nb.) Australia\nc.) New Zealand\n\n",
    "\n2.) Who is the current World Chess Champion\na.) Magnus Carlsen\nb.) Fabiano Caruana\nc.) Hikaru Nakamura\n\n",
    "\n3.) What is the capital of Georgia\na.) Baku\nb.) Tblisi\nc.) Tashkent\n\n",
];

questions = [
    Question(questionsData[0], "b"),
    Question(questionsData[1], "a"),
    Question(questionsData[2], "b"),
];

def runQuiz(questions) :
    score = 0;

    for question in questions :
        answer = input(question.promt);
        if answer == question.answer :
            score += 1;

    print("\nYou scored " + str(score) + " / " + str(len(questions)));

runQuiz(questions);

