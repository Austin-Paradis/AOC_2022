#Variable Creation
#rock = A
#paper = B
#scissors = C
#rock2 = X
#paper2 = Y
#scissors2 = Z
x_rock = 1
y_paper = 2
z_scissors = 3
win = 6
loss = 0
draw = 3
score = 0
score2 = 0

#Data Structure Creation
with open('input.txt') as d:
    for line in d.read().split("\n"):
        line = line.strip()
        they = line.split(' ')[0]
        you = line.split(' ')[1]

        #Part Two
        #Draw
        if they == "A" and you == "X":
            score2 = score2 + draw + x_rock
        elif they == "B" and you == "Y":
            score2 = score2 + draw + y_paper
        elif they == "C" and you == "Z":
            score2 = score2 + draw + z_scissors
        #Loss
        if they == "A" and you == "Z":
            score2 = score2 + loss + z_scissors
        elif they == "B" and you == "X":
            score2 = score2 + loss + x_rock
        elif they == "C" and you == "Y":
            score2 = score2 + loss + y_paper
        #Win
        if they == "A" and you == "Y":
            score2 = score2 + win + y_paper
        elif they == "B" and you == "Z":
            score2 = score2 + win + z_scissors
        elif they == "C" and you == "X":
            score2 = score2 + win + x_rock
        print("Total Score for Part Two: " + str(score2))
