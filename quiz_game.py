want_to_play = input("Do you want to play? ")
score = 0
if want_to_play.lower() != "yes":
    print("Okay see you later!")
    quit()

else:
    print("Welcome! Let's start the game.")
    print("You will get 5 points for each correct answer.\n")

answer1 = input("What is the full form of cpu? ")
if answer1.lower() == "central processing unit":
    score += 5
    print("Correct!")
else:
    print("Incorrect!")

answer2 = input("What is the full form of RAM? ")
if answer2.lower() == "random access memory":
    score += 5
    print("Correct!")
else:
    print("Incorrect!")

answer3 = input("What is the full form of PSU? ")
if answer3.lower() == "power supply":
    score += 5
    print("Correct!")
else:
    print("Incorrect!")

answer4 = input("What is the full form of PC? ")
if answer4.lower() == "personnal computer" or "personal computer":
    score += 5
    print("Correct!")
else:
    print("Incorrect!")

answer5 = input("What is the full form BD? ")
if answer5.lower() == "bangladesh":
    score += 5
    print("Correct!")
else:
    print("Incorrect!")

score_result = f"Your total score is {score}"
percentage = "You have obtained " + str((score/20)*100) + "% marks"

print(score_result)
if (score/4)*100 > 60:
    print(percentage)
else:
    print("You didn't pass!")
