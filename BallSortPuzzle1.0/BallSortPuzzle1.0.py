#Jessica Qinying Wu
#This is the recreation of the ball sort game programmed by python
#Project Start date: May 9th, 2020
#the puzzle board is represented by a 2D array using python list
#balls are put in tubes, which is a stack structute (FIFO)
#Balls are placed at the end of the nested lists when added and removed from the end of the list when popped

import random
import Puzzle
import GameFunctions
import time


def GameDescription():
    print('About this Game:')
    print('- The objective of this game is to sort balls according to their types')
    print('- Each ball is represented by a lower case ascii letter (i.e. a,b,c) as types. There are 4 balls for each ball type')
    print('- The balls are initially randomly arranged in different tubes, each tube can hold a maximum of 4 balls')
    print('- Move the balls across the tubes until all the tubes only hold one type of ball (the letters in each tube must be the same)')
    print('\n')

def InputHandling(cmd,game):
    if cmd=='R': #restarting the game
        print('Restarting the game ...')
        game.puzzle=copy.deepcopy(game.initPuzzle)
    
    elif cmd=='Q':
        return False
    else:
        print('Please enter a valid command as stated')
    return True


def NewPuzzle():
    print('Generating a new puzzle ...')
    return Puzzle.Puzzle(random.randint(Puzzle.MINIMUM_FILLED_TUBE,Puzzle.MAXIMUM_FILLED_TUBE),random.randint(1,2))


#entry point of the game
print('/nWelcome to the Ball Sort game/n')
GameDescription()
game=Puzzle.Puzzle(random.randint(Puzzle.MINIMUM_FILLED_TUBE,Puzzle.MAXIMUM_FILLED_TUBE),random.randint(1,2))
while True:
    startTime=time.time()
    isGameOn=True
    isGameFinished=False
    while isGameOn and not isGameFinished:
        game.PrintPuzzle()
        GameFunctions.Instructions(' (M) - Move a ball\n (S) - Shuffle the puzzle (R)\n - Restart the Game\n (N) - Start a new Game\n (D) - Read the game description\n (Q) - Quit the Game\n')
        cmd=input()
        if cmd=='M': #move ball
            print('Select a tube to remove a ball from by inputting its index as labeled on top of the tube (e.g. 3 for tube [3])N')
            origin=int(input()) #select a tube to remove a ball from
            while not (origin>=0 and origin<len(game.puzzle)):
                print('Invalid index, please select an index between 0 and %d inclusive' %(len(game.puzzle)-1))
                origin=int(input())
            print('Select a destination tube by inputting its index as labeled on top of the tube (e.g. 3 for tube [3]')
            destination=int(input()) #select a tube to move the ball to
            while not (destination>=0 and destination<len(game.puzzle)):
                print('Invalid index, please select an index between 0 and %d inclusive' %(len(game.puzzle)-1))
                destination=int(input())
            game.MoveBalls(origin,destination)
            isGameFinished=game.DetectWin() #detect whether the game is finished or not
        elif cmd=='S':
            game.ShuffleBalls()
        elif cmd=='D': #read the game description
            GameDescription()
        elif cmd=='N': #start a new puzzle
            del game
            game=NewPuzzle()
            break
        else:
            isGameOn=InputHandling(cmd,game)
        
    if not isGameOn: #quit game indication
        GameFunctions.QuitGameMessage()
        break
    if isGameFinished: #game finished and won
        game.PrintPuzzle()
        print('Total time used: %s' %GameFunctions.TimeUsed(startTime-time.time()))
        
        print('Well done! The balls are all sorted correctly! Do you want to ')
        response=''
        continueGame=True
        while not (response=='R' or response=='N' or response =='Q'):
            print('  (R) - Restart this game, or')
            print('  (N) - Start a new game, or')
            print('  (Q) - Quit the game?')
            response=input()
            if cmd=='N': #start a new puzzle
                del game
                game=NewPuzzle()
            else:
                continueGame=InputHandling(response,game)
        if continueGame==False:
            GameFunctions.QuitGameMessage()
            break
                




