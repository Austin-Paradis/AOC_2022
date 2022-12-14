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
        print(line)
        they = line.split(' ')[0]
        you = line.split(' ')[1]

        #Strategy Guide
        if they == "A" and you == "Y":
            score = score + win + y_paper
        elif they == "A" and you == "X":
            score = score + draw + x_rock
        elif they == "A" and you == "Z":
            score = score + loss + z_scissors
        elif they == "B" and you == "Y":
            score = score + draw + y_paper
        elif they == "B" and you == "X":
            score = score + loss + x_rock
        elif they == "B" and you == "Z":
            score = score + win + z_scissors
        elif they == "C" and you == "Y":
            score = score + loss + y_paper
        elif they == "C" and you == "X":
            score = score + win + x_rock
        elif they == "C" and you == "Z":
            score = score + draw + z_scissors
    print("Total Score: " + str((score)))


