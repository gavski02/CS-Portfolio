from random import randint

t = ["Rock", "Paper", "Scissors"];
computer = t[randint(0,2)];
try:
    input = raw_input
except NameError:
    pass

while(True):
    player = input("Rock, Paper, Scissors: ");
    computer = t[randint(0,2)];
    if player == computer:
        print("Tie!")
    elif player.lower() == "rock":
        if computer.lower() == "paper":
            print("You lose! " + computer + " covers " + player)
        else:
            print("You win! " + player + " smashes " + computer)
    elif player.lower() == "paper":
        if computer.lower() == "scissors":
            print("You lose! " + computer + " cut " + player)
        else:
            print("You win! " + player + " covers " + computer)
    elif player.lower() == "scissors":
        if computer.lower() == "rock":
            print("You lose... " + computer + " smashes " + player)
        else:
            print("You win! " + player + " cut " + computer)
    else:
        print("That's not a valid play. Check your spelling!")
