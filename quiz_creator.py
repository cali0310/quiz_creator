# pseudocode
# initialize the score and empty list
# ask user for question
# ask user for 4 possible answers (a, b, c, d)
# ask user for the correct answer (a, b, c, d)
# store questions, choices, and correct answer in a list
# loop until the user chooses to exit 
# save all questions in a text file

score = 0
quiz_list = []

while True:
    question = str(input("Enter a question (type 'x' to finish): "))
    if question.lower() == "x":
        break