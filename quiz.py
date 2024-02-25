questions = ("Which animal is known as the 'Ship of the Desert?: ",
             "How many days are there in a week?: ",
             "How many hours are there in a day?: ",
             "How many letters are there in the English alphabet?: ",
             "Rainbow consist of how many colours?: ")

options = (("A. Camel","B. Elephant","C. Lion","D. Tiger"),
           ("A. 7","B. 8","C. 6","D. 10"),
           ("A. 36","B. 69","C. 24","D. 12"),
           ("A. 25","B. 26","C. 27","D. 28"),
           ("A. 3","B. 4","C. 5","D. 7"))

answers = ("A","A","C","B","D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT!")

    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    question_num +=1

print("------------------")
print("   RESULTS   ")
print("------------------")


print("answer: ",end="")
for answer in answers:
    print(answer,end="")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess,end="")
print()

score=int(score/len(questions)*100)
print(f"Your score is: {score}%")
