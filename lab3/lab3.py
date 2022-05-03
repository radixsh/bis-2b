import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# https://www.w3schools.com/python/python_classes.asp

days = ['Day 4', 'Day 7', 'Day 10', 'Day 14', 'Day 21', 'Day 30']
width = 0.25

def blepharisma_high():
    normal_data = [10, 7, 26, 24, 138, 51]
    cannibal_data = [0, 0, 0, 2, 4, 1]
    
    fig = plt.figure()
    br1 = np.arange(len(normal_data)) + width
    br2 = [x + width for x in br1] 
    
    plt.bar(br1, normal_data, color="blue", width=width, edgecolor='grey', label='Normal' )
    plt.bar(br2, cannibal_data, color="red", width=width, edgecolor='grey', label='Cannibal')
    
    plt.xticks([r + width * 1.5 for r in range(len(normal_data))], days)
    plt.ylim(0, 140)
    plt.ylabel('Count') 
    plt.legend(["Normal", "Cannibals"], loc=2)
    
    plt.title("Blepharisma in high-nutrient environment")
    plt.savefig("high_resources.png", bbox_inches="tight")
    plt.show()

def blepharisma_low():
    normal_data = [3, 5, 6, 10, 4, 1]
    cannibal_data = [0, 0, 2, 2, 0, 0]
    
    fig = plt.figure()
    br1 = np.arange(len(normal_data)) + width
    br2 = [x + width for x in br1] 
    
    plt.bar(br1, normal_data, color="blue", width=width, edgecolor='grey', label='Normal' )
    plt.bar(br2, cannibal_data, color="red", width=width, edgecolor='grey', label='Cannibal')
    
    plt.xticks([r + width * 1.5 for r in range(len(normal_data))], days)
    plt.ylim(0, 140)
    plt.ylabel('Count') 
    plt.legend(["Normal", "Cannibals"], loc=2)
    
    plt.title("Blepharisma in low-nutrient environment")
    plt.savefig("low_resources.png", bbox_inches="tight")
    plt.show()

def cannibalism():
    high_relative_freqs = [0, 0, 0, 2.0 / 26.0, 4.0 / 142.0, 1.0 / 54.0]
    low_relative_freqs = [0, 0, 2.0/8.0, 2.0 / 12.0, 0, 0]
    
    
    fig = plt.figure()
    br1 = np.arange(len(high_relative_freqs)) + width
    br2 = [x + width for x in br1] 
    
    plt.bar(br1, high_relative_freqs, color="green", width=width, 
            edgecolor='grey', label='High-nutrient ratios')
    plt.bar(br2, low_relative_freqs, color="yellow", width=width, 
            edgecolor='grey', label='Low-nutrient ratios')
    
    plt.xticks([r + width * 1.5 for r in range(len(high_relative_freqs))], days)
    plt.ylim(0.0, 1.0)
    plt.ylabel('Ratio (cannibal:normal)') 
    plt.legend(["Cannibalism rate in high-nutrient environment", "Cannibalism rate in low-nutrient environment"], loc=2)
    
    plt.title("Cannibalism rates among Blepharisma")
    plt.savefig("cannibalism.png", bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    blepharisma_high()
    blepharisma_low()
    cannibalism()
