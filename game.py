import copy
import random
import math

VIC = 2 ** 10  # The value of a winning board (for max)
LOSS = -VIC  # The value of a losing board (for max)
TIE = 0  # The value of a tie
SIZE = 8  # The length of a winning sequence
COMPUTER = 2  # Marks the computer's cells on the board
HUMAN = 1  # Marks the human's cells on the board

'''
computer-lines, human-columns
computer-plus, human-minus
'''
'''
The state of the game is represented by a list of 4 items:
0. The game board - a matrix (list of lists) of ints. chosen cells = *,
1. The heuristic value of the state.
2. Who's turn is it: HUMAN or COMPUTER
3. The heuristic value of the state.
4. the row
5. the column
'''


def create():
    # Returns an empty board. The human plays first.

    # creates an 8*8 board with random numbers between -20 to 20
    # board = [['', '', 1, 2, 3, 4, 5, 6, 7, 8], [' ' for i in range(10)], [int(random.randint(-20, 21)) for i in range(8)] for j in range(8)]
    board = [[int(random.randint(-20, 20)) for i in range(8)] for j in range(8)]

    # returns beginning state- each state is[the board, humans score, computers score, the next row/column, who's next]
    return [board, 0.0, 0.0, int(random.randint(0, 7)), HUMAN]


def printState(s):
    # Prints the board. The empty cells are printed as numbers = the cells name(for input)
    # If the game ended prints who won.

    print('{:>3} {:>4} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3} {:>3}'.format(*['', 1, 2, 3, 4, 5, 6, 7, 8]))

    for r in range(len(s[0])):
        print("\n       -- -- -- -- -- -- -- -- -- -- -- --\n", end="")
        print(r+1 ,end="     |")
        for c in range(len(s[0][0])):
          if(s[0][r][c]==0.0001):
              print('*' ,"|", end="")
          else:
              print(s[0][r][c] ,"|", end="")
    print("\n       -- -- -- -- -- -- -- -- -- -- -- --\n")

        # print(*i)
    print("\n -- -- --\n Human score:{}\t Computer score:{}\n".format(s[1], s[2]))
    if isFinished(s):
        if s[2] > s[1]:
            print("Ha ha ha I won!")
        elif s[2] < s[1]:
            print("You did it!")
        else:
            print("It's a TIE")


def isFinished(s):
    # Returns True if the game ended
   if s[4] == HUMAN and s[0][s[3]] != SIZE * [0.0001]:  #if its humans turn but the row isnt all chosen
        return False
   elif s[4] == COMPUTER:
        for i in s[0]: #the column isnt full
            if i[s[3]] !=0.0001:
               return False
   return True

#זאת ההיוריסטיקה שלנו, היא מחושבת על ידי סכום המחשב פחות סכום הבנאדם
#כלומר, ה"ציון" שניתן לכל מצב על מנת לבדוק אם הוא כדאי מיוצג על ידי זה
#ככל שציון המחשב גבוה מבן האדם- יותר סיכוי לנצח
def value(s):
    # Returns the heuristic value of s
    if isFinished(s):
        if s[2] > s[1]: #VIC
            return math.pow(2, 10)
        elif s[2] < s[1]: #LOSS
            return -math.pow(2, 10)
        else:
            return 0
    else:
        return s[2] - s[1]


def isHumTurn(s):
    # Returns True if it the human's turn to play
    return s[4] == HUMAN


def whoIsFirst(s):
    # The user decides who plays first
    if int(input("Who plays first? 1-me / anything else-you. : ")) == 1:
        s[4] = COMPUTER
    else:
        s[4] = HUMAN




def makeMove(s, r, c):
    # Puts mark (for huma. or comp.) in r,c
    # switches turns
    # and re-evaluates the heuristic value.
    # Assumes the move is legal.
    s[s[4]] += s[0][r][c]  # adds value from tile to current player
    s[0][r][c] = 0.0001  # marks the board

    if s[4] == HUMAN:
        s[3] = c
    else:
        s[3] = r
    s[4] = COMPUTER + HUMAN - s[4]  # switches turns


def inputMove(s):
    # Reads, enforces legality and executes the user's move.
    printState(s)
    flag = True
    while flag:
        c = int(input("Enter column choice in row {}: ".format(s[3] + 1))) - 1
        r = s[3]
        if c < 0 or c >= SIZE or s[0][r][c] == 0.0001: #used place or out of range
            print("Ilegal move reenter please.")
        else:
            flag = False
            makeMove(s, r, c)

def sortBy(s):
    #returns the caculate value to sort
    return s[2] - s[1]


def getNext(s):
    # returns a list of the next states of s
    ns = []
    forced = s[3]
    if s[4] == HUMAN:
        for choice in range(SIZE):
            if s[0][forced][choice] != 0.0001:
                tmp = copy.deepcopy(s)
                makeMove(tmp, forced, choice)
                ns += [tmp]
        ns.sort(key=sortBy)

    else:
       for choice in range(SIZE):
            if s[0][choice][forced] != 0.0001:
                tmp = copy.deepcopy(s)
                makeMove(tmp, choice, forced)
                ns += [tmp]
       ns.sort(key=sortBy, reverse=True)

    return ns
