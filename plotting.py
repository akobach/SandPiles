import matplotlib.pyplot as plt 
import numpy as np



def sandpileplots(totalgrains, ntopples):
    # remove zero's from ntopples
    ntopples = [n for n in ntopples if n!=0]
    
    plt.plot(np.linspace(1, len(totalgrains), len(totalgrains)), totalgrains)
    plt.xlabel("move number")
    plt.ylabel("total grains of sand")
    plt.show()
    plt.clf()
    
    # plot histogram of ntopples
    bins = np.logspace(np.log10(1), np.log10(np.max(ntopples)), 20)
    heights, bins, _ = plt.hist(ntopples, bins=bins, log=True, density=True)
    
    # extract bin centers
    bin_centers = (bins[:-1] + bins[1:]) / 2

    # Plot the markers connected by lines
    plt.clf()
    plt.plot(bin_centers, heights, marker='o')
    
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True) 
    plt.xlabel("number of topples after a move")
    plt.ylabel("probability density")
    
    ymin = np.min(heights[np.nonzero(heights)])
    plt.ylim(10**(-1+int(np.log10(ymin))), 1) # end on major tick mark
    plt.xlim(1, 10**int(1+np.log10(bin_centers[-1]))) # end on major tick mark
    plt.show()