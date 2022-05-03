import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

days = [4, 7, 10, 14, 21, 30]

def blepharisma_high():
    days = ['Day 4', 'Day 7', 'Day 10', 'Day 14', 'Day 21', 'Day 30']
    high_normal_data = [10, 7, 26, 24, 138, 51]
    high_cannibal_data = [0, 0, 0, 2, 4, 1]
    
    width = 0.2
    fig = plt.figure()
    br1 = np.arange(len(high_normal_data))
    br2 = [x + width for x in br1] 
    
    plt.bar(br1, high_normal_data, color="blue", width=width, edgecolor='grey', label='Normal' )
    plt.bar(br2, high_cannibal_data, color="red", width=width, edgecolor='grey', label='Cannibal')
    
    plt.xticks([r + width for r in range(len(high_normal_data))], days)
    plt.ylabel('Count') 
    
    plt.title("Blepharisma in high-nutrient environment")
    plt.savefig("high_resources.png", bbox_inches="tight")
    plt.show()


def blepharisma_low():
    days = ['Day 4', 'Day 7', 'Day 10', 'Day 14', 'Day 21', 'Day 30']
    low_normal_data = [3, 5, 6, 10, 4, 1]
    low_cannibal_data = [0, 0, 2, 2, 0, 0]
    
    width = 0.2
    fig = plt.figure()
    br1 = np.arange(len(high_normal_data))
    br2 = [x + width for x in br1] 
    
    plt.bar(br1, high_normal_data, color="blue", width=width, edgecolor='grey', label='Normal' )
    plt.bar(br2, high_cannibal_data, color="red", width=width, edgecolor='grey', label='Cannibal')
    
    plt.xticks([r + width for r in range(len(high_normal_data))], days)
    plt.ylabel('Count') 
    
    plt.title("Blepharisma in low-nutrient environment")
    plt.savefig("low_resources.png", bbox_inches="tight")
    plt.show()


def cannibalism():
    fig, ax = plt.subplots(1, 1)
    ax.set_ylim([0.0, 1.0])

    high_relative_freqs = [0, 0, 0, 2.0 / 26.0, 4.0 / 142.0, 1.0 / 54.0]
    ax.bar(days, high_relative_freqs)

    low_relative_freqs = [0, 0, 2.0/8.0, 2.0 / 12.0, 0, 0]
    ax.bar(days, low_relative_freqs)

    plt.title("Cannibalism rates among Blepharisma")
    plt.savefig("cannibalism.png", bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    blepharisma_low()
    blepharisma_high()
    # cannibalism()
