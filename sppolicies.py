import abc
import random
from typing import Tuple


class SandPilePolicy:
    @abc.abstractmethod
    def get_move(self):
        raise NotImplementedError("Subclass needs to implement get_move()")
    

class ManualPolicy(SandPilePolicy):
    def __init__(self, pile):
        self.pile = pile
    
    def get_move(self) -> Tuple[int,int]:
        i,j = None, None
        while i is None:
            a = input("Where would you like to place sand? ")
            i,j = tuple(int(x) for x in a.split(","))
            if i%(self.pile.N-1)==0 or j%(self.pile.N-1)==0:
                i,j = None, None
                print("Cannot place sand on the edge of the pile. Try again.")
            
        return i,j
    

class RandomPolicy(SandPilePolicy):
    def __init__(self, pile):
        self.pile = pile
    
    def get_move(self) -> Tuple[int,int]:
        # do not place sand on the edge of the board
        return (random.randint(1, self.pile.N-2), random.randint(1, self.pile.N-2))
