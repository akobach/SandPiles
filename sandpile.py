import numpy as np
from collections import deque
from tqdm import tqdm
import plotting
import sppolicies
import itertools


class SandPile():
    def __init__(self, N: int, K: int):
        self.N = N # size of square sand pile
        self.K = K # critical height before a topple
        self.pile = np.zeros((self.N, self.N), dtype=int) # sand pile with zero sand to start
        self.queue= deque([]) # queuefor the sites that are ready to recieve sand
            

        
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
        while self.queue:
            # add grain to first element in queueand remove from queue
            k,l = self.queue.popleft()
            self.pile[k,l] += 1
            
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
        return i%(self.N-1)==0 or j%(self.N-1)==0 



    def get_neighbors(self, i: int, j: int):
        """
        Inputs i and j location of site
        Outputs generator of location of neighbors: (i+1,j), (i-1,j), (i,j+1), (i,j-1) 
        """
        yield (i+1,j)
        yield (i-1,j)
        yield (i,j+1)
        yield (i,j-1)

        
    def topple(self, i: int, j: int):
        """
        Topple site (i,j) by:
            Remove all grains from site (i,j)
            Distribute grains like a cycle of (up, down, right, left)
            If a neighbors gets a grain, add it to the queue
            Grains added to the border fall off
        """
        neighbor_iter = itertools.cycle(self.get_neighbors(i,j))
        while self.pile[i,j] > 0:
            k,l = next(neighbor_iter)
            if not self.is_border(k,l):
                self.queue.append((k,l))
                
            # sand is always lost, even if it goes off the edge
            self.pile[i,j] -= 1
            
            
     
     
     