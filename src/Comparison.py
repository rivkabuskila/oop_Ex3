import matplotlib.pyplot as plt
import numpy as np
size=1

plt.rc('font', size=6)
labels = ["|V|=11,|E|=22", "|V|=17 |E|=36", "|V|=31 |E|=80", "|V|=49 |E|=136", "|V|=40 |E|=102", "|V|=48 |E|=166"]
louding = [(0.002*size), (0.012 * size), (0.014 * size), (0.014 * size),  (0.015*size), (0.015*size)]
assists  = [0.007*size, 0.008*size,0.005*size,0.007*size,0.006*size,0.009*size]


x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
ax.bar(x - width, louding, width, label='python')
ax.bar(x, assists, width, label='java')

plt.xlabel('Graphs')
plt.ylabel('MS time')


ax.set_title('load')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.show()


labels1 = ["|V|=11,|E|=22", "|V|=17 |E|=36", "|V|=31 |E|=80", "|V|=49 |E|=136", "|V|=40 |E|=102", "|V|=48 |E|=166"]
louding1 = [(0.018*size), (0.029 * size), (0.157 * size), (0.149 * size),  (0.100*size), (0.171*size)]
assists1  = [0.031*size, 0.043*size,0.026*size,0.040*size,0.034*size,0.036*size]


x = np.arange(len(labels1))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
ax.bar(x - width, louding1, width, label='python')
ax.bar(x, assists1, width, label='java')

plt.xlabel('Graphs')
plt.ylabel('MS time')


ax.set_title('save')
ax.set_xticks(x)
ax.set_xticklabels(labels1)
ax.legend()

fig.tight_layout()

plt.show()

labels2 = ["|V|=11,|E|=22", "|V|=17 |E|=36", "|V|=31 |E|=80", "|V|=49 |E|=136", "|V|=40 |E|=102", "|V|=48 |E|=166"]
louding2 = [(0.002*size), (0.005 * size), ( 0.021 * size), (0.028 * size),  (0.015*size), (0.017*size)]
assists2  = [0.029*size, 0.035*size,0.022*size,0.028*size,0.037*size,0.027*size]


x = np.arange(len(labels2))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
ax.bar(x - width, louding2, width, label='python')
ax.bar(x, assists2, width, label='java')

plt.xlabel('Graphs')
plt.ylabel('MS time')


ax.set_title('Short Path')
ax.set_xticks(x)
ax.set_xticklabels(labels2)
ax.legend()

fig.tight_layout()

plt.show()


labels3 = ["|V|=11,|E|=22", "|V|=17 |E|=36", "|V|=31 |E|=80", "|V|=49 |E|=136", "|V|=40 |E|=102", "|V|=48 |E|=166"]
louding3 = [(0.002*size), ( 0.003 * size), ( 0.015 * size), (0.019 * size),  (0.020*size), (0.023*size)]
assists1  = [0.002*size, 0.012*size,0.022*size,0.008*size,0.018*size,0.014*size]


x = np.arange(len(labels3))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
ax.bar(x - width, louding3, width, label='python')
ax.bar(x, assists1, width, label='java')

plt.xlabel('Graphs')
plt.ylabel('MS time')


ax.set_title('center Point')
ax.set_xticks(x)
ax.set_xticklabels(labels3)
ax.legend()

fig.tight_layout()

plt.show()

labels4 = ["|V|=11,|E|=22", "|V|=17 |E|=36", "|V|=31 |E|=80", "|V|=49 |E|=136", "|V|=40 |E|=102", "|V|=48 |E|=166"]
louding4 = [(0.002*size), ( 0.013 * size), ( 0.019 * size), (0.014 * size),  (0.014*size), (0.014*size)]
assists1  = [0.003*size, 0.003*size,0.002*size,0.003*size,0.004*size,0.001*size]


x = np.arange(len(labels4))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
ax.bar(x - width, louding4, width, label='python')
ax.bar(x, assists1, width, label='java')

plt.xlabel('Graphs')
plt.ylabel('MS time')


ax.set_title('TSP')
ax.set_xticks(x)
ax.set_xticklabels(labels4)
ax.legend()

fig.tight_layout()

plt.show()