print("welcome to my computer quiz! ")

playing = input("Do you want to play? ")

if playing != "yes" :
    quit()


print("okay! let's play :) " )
score=0


answer=input("what does CPU stand for? ") 
if answer == "central processing unit":
    print("correct!")
    score+=1

else:
    print("Incorrect!")

answer = input("Who won 2025 Ipl?")
if answer == "RCB" :
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct" )




