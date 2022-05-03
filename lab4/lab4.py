import numpy as np
import matplotlib.pyplot as plt
import math
n = 8 # number of plants observed

# HEIGHTS 
fig = plt.figure()
plt.xlim(0, 4)
plt.xticks([0, 1, 2, 3, 4])
plt.xlabel("Treatment")
plt.ylim(0, 30)
plt.ylabel("Plant height (cm)")

# Treatment 1
treatment = 1
avg_g = 21.98 # green plants are, on average, 21.98 cm tall
stdev_g = 5.793
se_g = stdev_g / math.sqrt(n)
plt.plot(treatment, avg_g, marker='+')
plt.errorbar(treatment, avg_g, yerr=se_g, label="Green plants' height",
        color="green")

avg_y = 19.79 # yellow plants are, on average, 19.79 cm tall
stdev_y = 3.264 
se_y = stdev_y / math.sqrt(n)
plt.plot(treatment, avg_y, marker='+')
plt.errorbar(treatment, avg_y, yerr=se_y, label="Yellow-green plants' height",
        color="orange")

# Treatment 2
treatment = 2
avg_g = 21.78
stdev_g = 6.373 
se_g = stdev_g / math.sqrt(n)
plt.plot(treatment, avg_g, marker='+')
plt.errorbar(treatment, avg_g, yerr=se_g, label="Green plants' height",
        color="green")

avg_y = 17.17 
stdev_y = 3.181 
se_y = stdev_y / math.sqrt(n)
plt.plot(treatment, avg_y, marker='+')
plt.errorbar(treatment, avg_y, yerr=se_y, label="Yellow-green plants' height",
        color="orange")

# Treatment 3
treatment = 3
avg_g = 24.41 
stdev_g = 5.377 
se_g = stdev_g / math.sqrt(n)
plt.plot(treatment, avg_g, marker='+')
plt.errorbar(treatment, avg_g, yerr=se_g, label="Green plants' height",
        color="green")

avg_y = 16.06 
stdev_y = 4.557 
se_y = stdev_y / math.sqrt(n)
plt.plot(treatment, avg_y, marker='+')
plt.errorbar(treatment, avg_y, yerr=se_y, label="Yellow-green plants' height",
        color="orange")

plt.title("Height")
plt.savefig("height.png")
plt.show()


# FLOWERS 
fig = plt.figure()
plt.xlim(0, 4)
plt.xticks([0, 1, 2, 3, 4])
plt.xlabel("Treatment")
# plt.ylim(0)
plt.ylabel("Number of flowers and buds")

# Treatment 1
treatment = 1
avg_g = 30.5 # green plants are, on average, 21.98 cm tall
stdev_g = 18.0
se_g = stdev_g / math.sqrt(n)
plt.plot(treatment, avg_g, marker='+')
plt.errorbar(treatment, avg_g, yerr=se_g, label="Green plants' flowers",
        color="green")

avg_y = 6.916 # yellow plants are, on average, 19.79 cm tall
stdev_y = 8.537 
se_y = stdev_y / math.sqrt(n)
plt.plot(treatment, avg_y, marker='+')
plt.errorbar(treatment, avg_y, yerr=se_y, label="Yellow-green plants' flowers",
        color="orange")

# Treatment 2
treatment = 2
avg_g = 15.3 
stdev_g = 9.719 
se_g = stdev_g / math.sqrt(n)
plt.plot(treatment, avg_g, marker='+')
plt.errorbar(treatment, avg_g, yerr=se_g, label="Green plants' flowers",
        color="green")

avg_y = 19.8 
stdev_y = 11.19 
se_y = stdev_y / math.sqrt(n)
plt.plot(treatment, avg_y, marker='+')
plt.errorbar(treatment, avg_y, yerr=se_y, label="Yellow-green plants' flowers",
        color="orange")

# Treatment 3
treatment = 3
avg_g = 23.5 
stdev_g = 8.683 
se_g = stdev_g / math.sqrt(n)
plt.plot(treatment, avg_g, marker='+')
plt.errorbar(treatment, avg_g, yerr=se_g, label="Green plants' flowers",
        color="green")

avg_y = 16.7 
stdev_y = 11.7 
se_y = stdev_y / math.sqrt(n)
plt.plot(treatment, avg_y, marker='+')
plt.errorbar(treatment, avg_y, yerr=se_y, label="Yellow-green plants' flowers",
        color="orange")

plt.title("Flowers")
plt.savefig("flowers.png")
plt.show()


# ROOT MASS 
fig = plt.figure()
plt.xlim(0, 4)
plt.xticks([0, 1, 2, 3, 4])
plt.xlabel("Treatment")
plt.ylabel("Root mass (g)")

# Treatment 1
treatment = 1
avg_g = 0.679
stdev_g = 0.441 
se_g = stdev_g / math.sqrt(n)
plt.plot(treatment, avg_g, marker='+')
plt.errorbar(treatment, avg_g, yerr=se_g, label="Green plants' height",
        color="green")

avg_y = 0.564 
stdev_y = 0.451 
se_y = stdev_y / math.sqrt(n)
plt.plot(treatment, avg_y, marker='+')
plt.errorbar(treatment, avg_y, yerr=se_y, label="Yellow-green plants' height",
        color="orange")

# Treatment 2
treatment = 2
avg_g = 0.687 
stdev_g = 0.746 
se_g = stdev_g / math.sqrt(n)
plt.plot(treatment, avg_g, marker='+')
plt.errorbar(treatment, avg_g, yerr=se_g, label="Green plants' height",
        color="green")

avg_y = 0.264 
stdev_y = 0.242 
se_y = stdev_y / math.sqrt(n)
plt.plot(treatment, avg_y, marker='+')
plt.errorbar(treatment, avg_y, yerr=se_y, label="Yellow-green plants' height",
        color="orange")

# Treatment 3
treatment = 3
avg_g = 0.518 
stdev_g = 0.434
se_g = stdev_g / math.sqrt(n)
plt.plot(treatment, avg_g, marker='+')
plt.errorbar(treatment, avg_g, yerr=se_g, label="Green plants' height",
        color="green")

avg_y = 0.222 
stdev_y = 0.18 
se_y = stdev_y / math.sqrt(n)
plt.plot(treatment, avg_y, marker='+')
plt.errorbar(treatment, avg_y, yerr=se_y, label="Yellow-green plants' height",
        color="orange")

plt.title("Roots")
plt.savefig("roots.png")
plt.show()
