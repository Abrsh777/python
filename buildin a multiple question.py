from question import question

question_propmpts= ["what color are applies?\n(a) Red\green\n(b) Purple\n(c) Orange\n\n",
                    "what color are bananas?\n(a) Teal\n(b) Magneta\n(c) Yellow\n\n",
                     "what color are strawberries?\n(a)Yellow(b) Red\n(c) Blue\n\n",
                    
                    
                ]
questions = [
    question(question_propmpts[0],"a"),
    question(question_propmpts[1],"c"),
    question(question_propmpts[2],"b"),

]
def run_test (questions):
    score= 0
    for question in questions:
        answer = input(question.propmpts)
        if answer == question.answer:
            score += 1
    print ("you got" + str(score) + "\" + str(len(questions)) + ""correct" )
    run_test(questions)