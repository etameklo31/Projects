# a dictionary that stores question and answers
# have a variable that tracks the score of player
# loop through the dictionary using the key value pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1" : {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2" : {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3" : {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4" : {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5" : {
        "question": "What is the capital of Denmark?",
        "answer": "Copenhagen"
    }
}   

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print("Correct")
        score = score + 1
        print("Your score is: " + str(score))
        print("")
        print("")

    else:
        print("Wrong")
        print("The answer is : " + value['answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 5 questions correctly")
print("Your percentage is " + str(int(score/5 * 100)) + "%") 
print('')