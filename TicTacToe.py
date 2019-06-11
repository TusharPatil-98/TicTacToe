class GameController:
    score1 = 0
    score2 = 0
        
    def __init__(self,players):
        # Define the players
        self.players = players
        # Define who starts the game
        self.nplayer = 1        
        # Define the board
        self.board = [0] * 9
        self.winner = False
        pass
    
    # Show current position
    def show(self):
        print('\n'+'\n'.join([' '.join([['. ', 'O ', 'X '][self.board[3*j + i]] for i in range(3)]) for j in range(3)]))
        pass

    # Compute the score
    def scoring(self):
            print('Player 1 Score= %d \nPlayer 2 Score= %d' %(GameController.score1, GameController.score2))
           
            
    # Does the opponent have three in a line?
    def loss_condition(self):
        possible_combinations = [[1,2,3], [4,5,6], [7,8,9],
            [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
        
        return any(all((self.board[j-1] == self.nplayer) for j in i)for i in possible_combinations)
        
    def move(self):
        pos = int(input('Player %s, what do you play?\n' %(self.nplayer)))
        if self.board[pos-1] == 0:
            self.board[pos-1] = self.nplayer
        else:
            print('Invalid Move')
            self.move()

    def play(self):
        for i in range(0,9):            
            self.show()
            self.move()
            if self.loss_condition():
                self.show()
                print('Player %s Wins!!!\n\n' %(self.nplayer))
                self.winner = True
                if self.nplayer == 1:
                    GameController.score1 += 1
                else:
                    GameController.score2 += 1
                self.scoring()
                break       
            if self.nplayer == 1:
                self.nplayer = 2
            else:
                self.nplayer = 1
    
        if not self.winner:
            print('Draw!!!')
    
if __name__ == "__main__":
    while(True):
        GameController(2).play()
        if(input('\n\nRematch?(Y/n)\t') == 'n'):
            break

    print('\nHave A Nice Day!!!')
