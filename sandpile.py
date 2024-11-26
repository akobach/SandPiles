import numpy as np
from collections import deque
from tqdm import tqdm
import plotting
import sppolicies


class SandPile():
    def __init__(self, N: int, K: int):
        self.N = N # size of square sand pile
        self.K = K # critical height before a topple
        self.pile = np.zeros((self.N, self.N), dtype=int) # sand pile with zero sand to start
        self.queue = deque([]) # queue for the sites that are ready to recieve sand
            

        
    def play(self, Nturns: int, policy: sppolicies.SandPilePolicy, plot=False):
        """
        With the given policy, play Nturns of the game
        """
        
        totalgrains = [] # total number of grains in the pile after each move
        results = [] # each element is number of topples after each move
        
        # play Nturns times
        for _ in tqdm(range(Nturns)):
            
            # get the number of topples from playing a turn, with the given policy
            ntopples = self.turn(policy)
            
            # fill results lists only if plotting
            if plot:
                totalgrains.append(np.sum(self.pile))
                results.append(ntopples)
                
        # plot
        if plot:
            plotting.sandpileplots(totalgrains, results)
        
                
    
    def turn(self, policy: sppolicies.SandPilePolicy) -> int:
        """
        A single turn, given the policy.  
        Returns the total number of topples 
        """
        
        # counter for number of topples
        ntopples = 0
                
        # get which site to place next grain, given the policy
        i,j = policy.get_move()
                        
        # add site to queue
        self.queue.append((i,j))
                
        # loop through all sites ready to receive a grain of sand
        while len(self.queue) > 0:
            
            # add grain to last element in queue
            k,l = self.queue[-1]
            self.pile[k,l] += 1
            
            # remove site from queue
            self.queue.pop()
            
            # topple
            if self.pile[k,l] > self.K:
                self.topple(k,l)
                ntopples += 1
        
        return ntopples
    
    
    
    def is_border(self, i: int, j: int) -> bool:
        """
        input: i and j coordinates of site 
        output: True if site is on the border of the pile
                False otherwise
        """
        if i%(self.N-1)==0 or j%(self.N-1)==0:
            return True
        else:
            return False



    def get_neighbors(self, i: int, j: int) -> list:
        """
        Inputs i and j location of site
        Outputs list of tuples [(i+1,j), (i-1,j), (i,j+1), (i,j-1)] for location of neighbors
        """
        return [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]


        
    def topple(self, i: int, j: int):
        """
        Topple site (i,j) by:
            Remove 4 grains from site (i,j)
            Add neighbors (if not on border) to queue
        """
        self.pile[i,j] -= 4
        for k,l in self.get_neighbors(i,j):
            if not self.is_border(k,l):
                self.queue.append((k,l))
     