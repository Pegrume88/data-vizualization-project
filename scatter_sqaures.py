import matplotlib.pyplot as plt


x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# set chart title and label axes
ax.set_title("Sqaure Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Sqaure Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# set the range for each axis.abs
ax.axis([0, 1100, 0, 1100000])

plt.show()

