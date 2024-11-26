import sandpile as sp
import sppolicies
import cProfile
    

if __name__ == "__main__":
     
    # initialize pile
    pile = sp.SandPile(N=100, K=3)
    
    # policy to place the grains of sand at random locations on the pile
    randompolicy = sppolicies.RandomPolicy(pile)
    
    # burn in to equilibrum
    pile.play(Nturns=5*10**4, policy=randompolicy, plot=False)
    
    # collect statistics
    pile.play(Nturns=5*10**4, policy=randompolicy, plot=True)

    # profiling
    #cProfile.run('pile.play(Nturns=5*10**4, policy=randompolicy)')
        