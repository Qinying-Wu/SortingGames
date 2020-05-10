import random
import string
import copy

TUBE_CAPACITY=4 #the max capacity of each tube is 4 balls
MINIMUM_FILLED_TUBE=3 #the minimum number of filled tubes in a game is 3
MAXIMUM_FILLED_TUBE=13 #the maximum number of filled tubes in a game is 26 (half the number of alphabets that exist)
UNFILLED_SPACE='-' #represents the unfilled space in a tube

#the puzzle object class
#contains three member variables
#  member variable 1: puzzle - the puzzle board of the sort game
#  member variable 2: filledTubes - the count of tubes that should be filled with balls up to the TUBE_CAPACITY in the game
#  member variable 3: emptyTubes - the count of idle tubes for moving the balls
class Puzzle:
    #constructor - a puzzle object has three attributes: the puzzle board, the count of filled tubes, and the count of empty tubes
    def __init__(self, filledTubes, emptyTubes):
        self.filledTubes=filledTubes
        self.emptyTubes=emptyTubes
        self.MakePuzzle()
    #function to make the puzzle board
    #parameter filledTubes is the number of tubes each to be fully filled with the same kind of balls in the game
    #returns the generated game puzzle
    def MakePuzzle(self):
        self.puzzle=[]
        print('filled tubes: %d' %self.filledTubes)
        print('empty tubes: %d' %self.emptyTubes)
        for count in range(self.filledTubes): #initialize the puzzle with the number of filled tubes
            self.puzzle.append([])
        for alphabet in string.ascii_lowercase[:self.filledTubes]: #randomly put balls represented by letters in each tube
            for i in range(TUBE_CAPACITY):
                tubeIndex=random.randint(0,self.filledTubes-1) #randomly generate a tube index to put the ball in each tube
                while len(self.puzzle[tubeIndex])>=TUBE_CAPACITY:
                    tubeIndex=random.randint(0,self.filledTubes-1) #keep searching for unfilled tubes while the current one is fully filled
                self.puzzle[tubeIndex].append(alphabet)
        self.ShuffleBalls()
        for empty in range(self.emptyTubes):
            self.puzzle.append([])#add empty tubes to the puzzle for moving
        random.shuffle(self.puzzle)#randomly shuffle the puzzle
        self.initPuzzle=copy.deepcopy(self.puzzle) #save a copy of the initial board for restarting the game
   
    #function to furthe randomize the arrangement of balls
    def ShuffleBalls(self):
         for tube in self.puzzle: #further randomize the puzzle
            random.shuffle(tube)
         random.shuffle(self.puzzle)
    #function to move balls to different tubes in the game to sort them
    #parameter puzzle is the current game board
    #parameter origin is the index of the original tube that the ball resides in
    #parameter destination is the index of the destination tube that the ball is going to be moved to
    def MoveBalls(self,origin,destination):
        #only move a ball if the origin tube is non-empty and the destination tube is not full
        #if any(ball!=UNFILLED_SPACE for ball in puzzle[origin]) and UNFILLED_SPACE in puzzle[destination]:
        if len(self.puzzle[origin])>0 and len(self.puzzle[destination])<TUBE_CAPACITY:
               self.puzzle[destination].append(self.puzzle[origin].pop())
        else:
            #case: the origin is empty
            if len(self.puzzle[origin])==0:
                print("INVALID MOVE: No balls are present in the origin tube %d, please select another origin tube with at least one ball in it\n" %origin)
            #case: the destination is full
            if len(self.puzzle[destination])==TUBE_CAPACITY:
                print("INVALID MOVE: The destination tube %d is already full, please select another destination tube that contains three or less balls in it\n" %destination)

    #function to print the puzzle of the ball sort game
    def PrintPuzzle(self):
        for base in range(self.filledTubes+self.emptyTubes):
            print((' [ %d] '%base) if base <10 else ' [%d] '%base,end="")
        print('\n')
        for row in range(TUBE_CAPACITY):
            for tubes in range(self.filledTubes+self.emptyTubes):
                print(' | %s| ' %(self.puzzle[tubes][TUBE_CAPACITY-row-1] if (TUBE_CAPACITY-row)<=len(self.puzzle[tubes]) else UNFILLED_SPACE),end="")
            print('\n')
        for base in range(self.filledTubes+self.emptyTubes):
            print(' ____ ',end="")
        print('\n')
    #function to determine whether the game is won or not
    #returns true if all the balls are sorted such that all balls of the same type are stored in one tube only, and false otherwise
    def DetectWin(self):
        for tube in self.puzzle:
            if len(tube)>0:
                if len(tube)<TUBE_CAPACITY| len(set(tube))>1: #(not fully filled tube) or (fully filled tube and not unique balls)
                    print(set(tube))
                    return False
        return True
