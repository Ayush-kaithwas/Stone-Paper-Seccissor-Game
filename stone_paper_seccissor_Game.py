import random

user = 0
computer = 0


def random_input():
    lst = ["Rock", "Paper", "Scissor"]
    a = random.choice(lst)
    return a


i = 0
while i < 5:
    print("Choose one to play this game")
    print("S for Scissor\nR for Rock\nP for Paper")
    temp = str(input()).capitalize()
    i = i + 1
    if temp == "R":
        a = random_input()
        print("Computer =", a)

        if str(a) == "Rock":
            print("tie")
            user = user + 0
            computer = computer + 0

        elif str(a) == "Paper":
            print("you loose")
            computer = computer + 1
            user = user + 0

        elif str(a) == "Scissor":
            print("You won")
            user = user + 1
            computer = computer + 0

        print("user = ", user)
        print("Computer = ", computer)

    # Paper
    elif temp == "P":
        a = random_input()
        print("Computer =", a)

        if str(a) == "Rock":
            print("you won")
            user = user + 1
            computer = computer + 0

        elif str(a) == "Paper":
            print("tie")
            computer = computer + 0
            user = user + 0

        elif str(a) == "Scissor":
            print("You loose")
            user = user + 0
            computer = computer + 1

        print("user = ", user)
        print("Computer = ", computer)

    # Scissor

    if temp == "S":
        a = random_input()
        print("Computer =", a)

        if str(a) == "Rock":
            print("you loose")
            user = user + 0
            computer = computer + 1

        elif str(a) == "Paper":
            print("you Won")
            computer = computer + 0
            user = user + 1

        elif str(a) == "Scissor":
            print("Tie")
            user = user + 0
            computer = computer + 0

        print("user = ", user)
        print("Computer = ", computer)

    print("Chances left = ", (5 - i))

if user > computer:
    print("Congratulations you win")
elif user == computer:
    print("Match tied")

elif computer > user:
    print("You loose")

print(f"Total score is computer = {computer} and user ={user}")
