file1 = open('input.txt', 'r')
Lines = file1.readlines()


def validgame(line, r, g, b):
    sets = line[9:].strip().split(";")
    for s in sets:
        c = s.split(",")
        cubes = " ".join(c).split(" ")
        cubes = list(filter(None, cubes))
        for i in range(len(cubes) - 1, 0, -2):
            if cubes[i] == "red":
                if int(cubes[i - 1]) > r:
                    return False
            elif cubes[i] == "green":
                if int(cubes[i - 1]) > g:
                    return False
            elif cubes[i] == "blue":
                if int(cubes[i - 1]) > b:
                    return False
    return True


def sumofpowersets(line):
    game = line[line.index(":")+1:].strip().split(";")
    game = "".join(game).replace(",", "").split(" ")
    list(filter(None, game))
    dict = {"red": 0, "green": 0, "blue": 0}
    for i in range(len(game) - 1, 0, -2):
        if dict.get(game[i]) < int(game[i - 1]):
            dict[game[i]] = int(game[i - 1])
    total = 1
    for i in dict.values():
        total *= i
    return total


sumOfGames = 0
powerOfGames = 0
lineNumber = 1
r = 12
g = 13
b = 14
for line in Lines:
    if validgame(line, r, g, b):
        sumOfGames += lineNumber

    powerOfGames += sumofpowersets(line)
    lineNumber += 1
print(sumOfGames)
print(powerOfGames)
