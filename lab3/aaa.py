import matplotlib as mpl
import matplotlib.pyplot as plt

class BlepharismaGraph:
    def __init__(self):
        self.fig, self.ax = plt.subplots(1, 1)
        self.ax.set_ylim([0, 150])
        self.data
    def set_title(title):
        self.ax.set_title(title)


if __name__ == "__main__":
    high_normal = BlepharismaGraph()

    days = [4, 7, 10, 14, 21, 30]
    high_normal.data = [
            1+1+2+1+1+4,
            1+1+1+2+1+1,
            2+2+1+2+3+4+2+2+2+4+1+1,
            4+1+1+4+2+1+1+2+1+4+1+2,
            11+7+9+13+10+12+14+10+10+11+7+8+6+8+2,
            3+4+5+2+3+2+5+3+5+9+2+2+4+2
            ]
    high_normal.ax.plot(days, high_normal_data, color="blue", label="Normal population")
    
    high_cannibal.data = [0, 0, 0, 2, 4, 1]
    high_cannibals = ax.plot(days, high_cannibal_data, color="red", label="Cannibal population")

    high.set_title = "Blepharisma in high-nutrient environment"
    ax.legend(bbox_to_anchor=(1, 1), loc="upper left")
    plt.savefig("high_resources.png", bbox_inches="tight")
    plt.show()


    fig, ax = plt.subplots(1, 1)
    low_normal_data = [
            1+1+1,
            1+1+1+1+1,
            1+1+1+2+1,
            1+3+1+2+2+1,
            2+1+1,
            1
            ]
    low_normals = ax.plot(days, low_normal_data, color="blue", label="Normal population")
    
    low_cannibal_data = [0, 0, 2, 2, 0, 0]
    low_cannibals = ax.plot(days, low_cannibal_data, color="red", label="Cannibal population")

    ax.set_title = "Blepharisma in low-nutrient environment"
    ax.set_ylim([0, 150])
    ax.legend(bbox_to_anchor=(1, 1), loc="upper left")
    plt.savefig("low_resources.png", bbox_inches="tight")
    plt.show()
