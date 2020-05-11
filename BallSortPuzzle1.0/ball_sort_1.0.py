#Jessica Qinying Wu
#This is the recreation of the ball sort game programmed by python
#Project Start date: May 9th, 2020
#the puzzle board is represented by a 2D array using python list
#balls are put in tubes, which is a stack structute (FIFO)
#Balls are placed at the end of the nested lists when added and removed from the end of the list when popped

import random
import puzzle
import game_functions
import time
import copy


def game_description():
    print('About this Game:')
    print('- The objective of this game is to sort balls according to their types')
    print('- Each ball is represented by a lower case ascii letter (i.e. a,b,c) as types. There are 4 balls for each ball type')
    print('- The balls are initially randomly arranged in different tubes, each tube can hold a maximum of 4 balls')
    print('- Move the balls across the tubes until all the tubes only hold one type of ball (the letters in each tube must be the same)')
    print('\n')

def input_handling(cmd,game):
    if cmd=='R': #restarting the game
        print('Restarting the game ...')
        game._Puzzle__puzzle=copy.deepcopy(game._Puzzle__init_puzzle)
    
    elif cmd=='Q':
        return False
    else:
        print('Please enter a valid command as stated')
    return True

#function to create a new puzzle by further complicating the randomizing algorithm
#(if a tube has less than two types of ball in the initial puzzle, generate the puzzle again)
#return the generated puzzle
def new_puzzle():
    print('Generating a new puzzle ...')
    temp_puzzle=puzzle.Puzzle(random.randint(puzzle.MINIMUM_FILLED_TUBE,puzzle.MAXIMUM_FILLED_TUBE),random.randint(1,2))
    while any((len(set(tube))<2 and len(tube)>0) for tube in temp_puzzle._Puzzle__puzzle):
        temp_puzzle=puzzle.Puzzle(random.randint(puzzle.MINIMUM_FILLED_TUBE,puzzle.MAXIMUM_FILLED_TUBE),random.randint(1,2))

    return temp_puzzle

#entry point of the game
print('/nWelcome to the Ball Sort game/n')
game_description()
game=new_puzzle()
while True:
    start_time=time.time()
    is_game_on=True
    game_finished=False
    while is_game_on and not game_finished:
        game.print_puzzle()
        game_functions.print_instruction(' (M) - Move a ball\n (S) - Shuffle the puzzle\n (R) - Restart the Game\n (N) - Start a new Game\n (D) - Read the game description\n (Q) - Quit the Game\n')
        cmd=input()
        if cmd=='M': #move ball
            print('Select a tube to remove a ball from by inputting its index as labeled on top of the tube (e.g. 3 for tube [3])N')
            origin=int(input()) #select a tube to remove a ball from
            while not (origin>=0 and origin<len(game._Puzzle__puzzle)):
                print('Invalid index, please select an index between 0 and %d inclusive' %(len(game._Puzzle__puzzle)-1))
                origin=int(input())
            print('Select a destination tube by inputting its index as labeled on top of the tube (e.g. 3 for tube [3]')
            destination=int(input()) #select a tube to move the ball to
            while not (destination>=0 and destination<len(game._Puzzle__puzzle)):
                print('Invalid index, please select an index between 0 and %d inclusive' %(len(game._Puzzle__puzzle)-1))
                destination=int(input())
            game.move_balls(origin,destination)
            game_finished=game.detect_win() #detect whether the game is finished or not
        elif cmd=='S':
            game.shuffle_balls()
        elif cmd=='D': #read the game description
            game_description()
        elif cmd=='N': #start a new puzzle
            del game
            game=new_puzzle()
            break
        else:
            is_game_on=input_handling(cmd,game)
        
    if not is_game_on: #quit game indication
        game_functions.quit_game_message()
        break
    if game_finished: #game finished and won
        game.print_puzzle()
        print('Total time used: %s' %game_functions.time_used(start_time-time.time()))
        
        print('Well done! The balls are all sorted correctly! Do you want to ')
        response=''
        continue_game=True
        while not (response=='R' or response=='N' or response =='Q'):
            print('  (R) - Restart this game, or')
            print('  (N) - Start a new game, or')
            print('  (Q) - Quit the game?')
            response=input()
            if cmd=='N': #start a new puzzle
                del game
                game=new_puzzle()
            else:
                continue_game=input_handling(response,game)
        if continue_game==False:
            game_functions.quit_game_message()
            break
                




