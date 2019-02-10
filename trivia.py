import time
import sys

responseList=["Yes", "yes", "YES", "Yesh"]
seconds = 10
timer = 5


print("Hello, Welcome to Trivia! \n")
print("Are you Ready to play? ")
response = input("  1 for yes      |||     2 for No  ")
int(response)

if (response == 2):
    print("Come back when you are ready ")
    sys.exit


if (response == 1):
        print("Great Let's get ready to play! ")
        for i in range (seconds):
            if (i < 7):
                print(str(seconds - i) + " seconds til game begins")
            else:
                print(str(seconds - i)+ " SECONDS TIL GAME STARTS!!!")

            time.sleep(1)



score = 0
answers = [1, 2, 3]


answers=input("Which of the following was not an OG colorway ? \n 1.) Royals \n 2.) Breds \n 3.) Pine Greens\n" )
if (answers == 3):
    score = score + 1



answers= input("How many rings does Micheal Jordan have?\n 1.) 3 \n 2.) 5 \n 3.) 6 \n ")
if (answers == 3):
    score = score + 1



answers= input("Which is a subsidary brand of Nike? \n 1.) Fila \n 2.) Hurley \n 3.) Puma \n " )
if (answers == 2):
    score = score + 1


answers= input("Who designed the Jordan 3? \n 1.) Lewis Armstrong \n 2.) Bobby Porter \n 3.) Tinker Hatfield \n")
if (answers == 3):
    score = score + 1


if (answers > 3 ):
    print("Congrats! Your score is " + str(score) + "/4 ! \n")
    time.sleep(1)
else:
    print("Your score is "+ str(score)  + "/4 \n ")
    time.sleep(1)


print("Thank you for playing! ")
time.sleep(1)
