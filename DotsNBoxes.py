from random import *
import collections
from Algorithm import *
from Board import *
from Nodes import *


class DotsNBoxes: 
    def __init__(self, Board_Xdim, Board_Ydim, Ply_num):
        currentState = Game([], Board_Xdim, Board_Ydim)
        currentState.Initiate()
        self.State = Thing(currentState)
        self.Ply_num = Ply_num
        self.Score = 0

    def Human(self): 
        self.State.Draw()

        HumanX = int(input("Please enter the 'X' coordinate of your choice: "))
        HumanY = int(input("Please enter the 'Y' coordinate of your choice: "))
        if (HumanX, HumanY) not in self.State.children:
            self.State.Make(HumanX, HumanY, False)
            self.State = self.State.children[(HumanX, HumanY)]
        else:
            self.State = self.State.children[(HumanX, HumanY)]

        print("Current Score =====>> Your Score - AI Score = " + str(self.State.CurrentScore),end ="\n\n\n")

        self.Computer()


    def Computer(self): 
        self.State.Draw()

        move = Algo.miniMax(self.State, self.Ply_num)

        self.State = self.State.children[(move[0], move[1])]

        print("AI selected the following coordinates to play:\n" + "(" ,str(move[0]), ", " + str(move[1]), ")", end = "\n\n")

        print("Current Score =====>> Your Score - AI Score = " + str(self.State.CurrentScore), end = "\n\n\n")

        if len(self.State.children) == 0:
            self.State.Draw()
            self.Evaluation()
            return

        self.Human()

    def Evaluation(self): 
        print("Session ended.\n")
        if self.State.CurrentScore > 0:
            print("You win!")
            exit()
        elif self.State.CurrentScore < 0:
            print("You lose.")
            exit()
        else:
            print("Drawn")
            exit()

    def start(self):
        self.Human()
