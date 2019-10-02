from random import randint;

try:
    input = raw_input;
except NameError:
    pass;

numColors = 8;
colors = ["R","G","B","O","Y","BL","BR","W"];

def getPlayerInput():
    color1 = input("guess a color using letters R, G, B, BL, O, Y, BR, W: ").upper();
    color2 = input("guess a color using letters R, G, B, BL, O, Y, BR, W: ").upper();
    color3 = input("guess a color using letters R, G, B, BL, O, Y, BR, W: ").upper();
    color4 = input("guess a color using letters R, G, B, BL, O, Y, BR, W: ").upper();
    return [color1, color2, color3, color4];

def getRandomSequence():
    return [colors[randint(0,7)], colors[randint(0,7)], colors[randint(0,7)], colors[randint(0,7)]]

def playLoop():
    global attempts;
    playerGuess = getPlayerInput();
    arr = [];
    for i in range(len(sequence)):
        if(sequence[i] == playerGuess[i]):
            arr.append("C");
            continue
        elif(playerGuess[i] != sequence[i] and playerGuess[i] not in sequence):
            arr.append("0");
            continue;

    for i in range(4):
        if(playerGuess[i] != sequence[i] and playerGuess[i] in sequence):
            arr.append("B");
            continue

    if(arr == ["C","C","C","C"]):
        print("You Win");
        break;
    elif(attempts == 0):
        print("Ran Out off attempts");
        break;
    else:
        attempts = attempts - 1;
        print("you have " + str(attempts) + " attempts left");


    return arr;

sequence = getRandomSequence();
playerGuess = [];

def play():
    message = ''.join(playLoop());
    global attempts;

    print(message);

    if(attempts != 0):
        play();

attempts = 8;
play();
print(playerGuess);
print(sequence);
