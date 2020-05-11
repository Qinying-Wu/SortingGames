#Jessica Qinying Wu
#This is the file containing the general functions to run a game

import time
#function to print the input command instructions of a game
#parameter options is the different inputs in the game
def print_instruction(options):
    print('Input Command Instructions/n')
    print(options)
    print('More input prompts will follow (if any) afterwards\n')

#function to display the message if the player decides to quit the game
def quit_game_message():
    print('You are exitting the game, hope to see you next time!')

    
#function to calculate the time used to finish the game
#parameter sec is the total time used in seconds
#returns the time used as a string in the format [h]hours:[m]minutes:[s]seconds
def time_used(secs):
    minutes=int(secs/60)
    hours=int(minutes/60)
    seconds=secs%60
    result='%d seconds' %seconds
    if hours>0:
        results='%d hours % minutes '%(hours, minutes)+result
    else:
        if minutes>0:
            result='%d minutes '%minutes+result
    return result