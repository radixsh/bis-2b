import matplotlib as mpl
import matplotlib.pyplot as plt
import sys

runs = [x for x in range(0, 8)]

# a = [4, 6, 6, 9, 9, 9, 10, 12]
# b = [3, 4, 7, 8, 9, 11, 12, 13]
c = [2, 3, 6, 9, 10, 11, 13, 15]
d = [1, 2, 2, 6, 8, 8, 9, 9]
# e = [3, 4, 7, 15, 18, 18, 18, 18]
# f = [6, 9, 14, 16, 18, 18, 20, 21]


plt.scatter(runs, c, color="orange", label="Group C")
plt.scatter(runs, d, color="blue", label="Group D")

plt.xlabel('Samples taken')
plt.ylabel('Total number of species observed')

plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.savefig("succulents.png", bbox_inches="tight")
plt.show()

# plt.scatter(runs, f_new_species, color="yellow")
#     ref_l = ax.plot(x_vals, ref_stats_linear, color="orange", label="Reference (linear)")
#     ref_b = ax.plot(x_vals, ref_stats_binary, color="orange", label="Reference (binary)", linestyle='--')
#     my_l = ax.plot(x_vals, my_stats_linear, color="blue", label="My statistics (linear)")
#     my_b = ax.plot(x_vals, my_stats_binary, color="blue", label="My statistics (binary)", linestyle='--')
#     # https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html
# ax.legend(bbox_to_anchor=(1,1), loc="upper left")
# plt.savefig(picname, bbox_inches="tight")
# plt.xlabel('Samples taken by Group F')
# plt.ylabel('Total number of species observed')
# 
# plt.savefig("f.png", bbox_inches="tight")
# plt.show()

