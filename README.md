# Playing Games in Sand Piles

Currently, this code only implements a BTW abelian sand pile model with a random policy.

The external Python libraries used are (included also is a `.yml` file for creating a venv.):
* numpy
* matplotlib
* tqdm

Within `main.py` there are a few configs things to fiddle with:
* a pile object can be initialized like this: `pile = sp.SandPile(N=100, K=3)` for a _NxN_ pile and where a site will topple if it has > _K_ grains of sand.  The pile starts out with zero grains of sand.
* a random policy is initialized as follows: `randompolicy = sppolicies.RandomPolicy(pile)`.  The policy depends on the pile, since it needs to see the pile know where to place a grain of sand.  (For this random policy, it only needs to know where the edges are.)
* the line `pile.play(Nturns=10**5, policy=randompolicy, plot=True)` will place a single grain of sand on the pile, `Nturns` times, and record the number of topplings that each move causes.  If `plot=True`, then two plots will pop up at the end of the run that visualize: 
    * the number of grains of sand on the pile after each move
    * the probability density for the number of topples after a single move

To run the code:

`>> python main.py`





