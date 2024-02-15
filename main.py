from Algorithm import *
from DotsNBoxes import *
from Board import *
from Nodes import *

def main():
    while True:

        print("\t\tWelcome to the game of Dots and Boxes!1\n\n\n")

        x = input("Press 1 to start the game or press 2 to exit\n\n")
        if x == "1":
                
            Board_Xdim = int(input("\nPlease enter the number of rows for the board: \n")) * 2 + 1

            if Board_Xdim < 5:
                print("\nthe number of rows should atleast be 2\n")
                exit()

            Board_Ydim = int(input("\nPlease enter the number of columns for the board: \n")) * 2 + 1

            if Board_Ydim < 5:
                print("\nthe number of columns should atleast be 2\n")
                exit()

            Ply_num = int(input("\nPlease enter the number of ply's used by the AI: \n"))

            if Ply_num < 2:
                print("\nThe number of plies should be higher than 1\n")
                exit()

            Match = DotsNBoxes(Board_Xdim, Board_Ydim, Ply_num)
            Match.start()
        else: 
            print ("\n\nSession ended.")
            exit()
            
if __name__ == "__main__":
    main()