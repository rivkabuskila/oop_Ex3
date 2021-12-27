import matplotlib.pyplot as plt
import numpy as np
size=100

plt.rc('font', size=6)
labels = ["load", "save", "short path", "center", "tsp"]
louding = [(0.062*size), (87.064 * size), (0.073 * size), (11.911 * size),(0.163*size)]
assists  = [0.030*size, 100.548*size,0.065*size,100.084*size,0.010*size]


x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
ax.bar(x - width, louding, width, label='python')
ax.bar(x, assists, width, label='java')

plt.xlabel('Graphs')
plt.ylabel('MS time')


ax.set_title('1,000 node')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.show()


plt.rc('font', size=6)
labels1 = ["load", "save", "shortpath", "center", "tsp"]
louding1 = [(0.891*size), (205.650 * size), (0.571 * size), (3000.000 * size),  (1.923*size)]
assists1  = [0.132*size, 400.052*size,0.139*size,400.003*size,0.238*size]


x = np.arange(len(labels1))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
ax.bar(x - width, louding1, width, label='python')
ax.bar(x, assists1, width, label='java')

plt.xlabel('Graphs')
plt.ylabel('MS time')


ax.set_title('10,000 node')
ax.set_xticks(x)
ax.set_xticklabels(labels1)
ax.legend()

fig.tight_layout()

plt.show()



plt.rc('font', size=6)
labels2 = ["load", "shortpath","tsp"]
louding2 = [(18.872*size), (14.826 * size),  (43.979*size)]
assists2  = [06.179*size, 02.658*size,  5.634*size]


x = np.arange(len(labels2))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
ax.bar(x - width, louding2, width, label='python')
ax.bar(x, assists2, width, label='java')

plt.xlabel('Graphs')
plt.ylabel('MS time')


ax.set_title('100,000 node')
ax.set_xticks(x)
ax.set_xticklabels(labels2)
ax.legend()

fig.tight_layout()

plt.show()
