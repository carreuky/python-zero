
#contain commone implemeation details between other classes

class AbstractGame: #don't make instances of it
    #methods needs to be as gernal as a possible
    @staticmethod
    def start(self):
        while True:
            start = input("wona play")
            if start.lower() == 'yeah':
                break;
            
        self.play()
    @staticmethod
    def end(self):
        print('you are done')
        self.rest()
        
    def play(self):
        raise NotImplementedError("provide implemation for play")
    
    def reset(self):
        raise NotImplementedError('reset implemation')
    
import random 
class RandomGuesser(AbstractGame):
     def __init__(self,rounds):
         self.rounds = rounds
         self.round =0
        
     def reset(self):
        self.round = 0
        
     def play( self):
         while self.round < self.rounds:
             self.round +=1
             print(f"welcome to round {self.round}")
             random_num= random.randint(0,10)
             while True:
                 guess = input("Enter a number 1-10: ")
                 if int(guess) == random_num:
                     print('you got it')
                     break;
         self.end()
         
g=RandomGuesser(1)
g.play()