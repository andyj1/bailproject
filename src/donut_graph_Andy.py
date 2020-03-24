import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.axis('equal')            # axis scale
cm = plt.get_cmap("Pastel1")  # color map

# outer pie (participants)
cout = cm([1, 3, 5, 7])
width1 = 0.5
data1 = [175, 47, 50, 63]
labels1 = ['Red Hook on the Road', 'Brooklyn Networks',
           'Brooklyn Woods', '"Made in NY" PA']
pie, _ = ax.pie(data1, radius=1, colors=cout,
                startangle=90,
                labels=data1, labeldistance=0.65)
plt.setp(pie, width=width1, edgecolor='white')

# inner pie (completion)
cm = plt.get_cmap("tab20c")  # color map
cin = cm(np.array([10, 1000, 10, 1000, 10, 1000, 10, 1000]))
width2 = 0.1
data2 = list([175*0.9, 175*0.1, 47*0.6, 47*0.4,
              50*0.6, 50*0.4, 63*0.81, 63*0.19])
data_label2 = list([90, '', 60, '',
                    60, '', 81, ''])
units = list(['%', '']*4)
labels2 = list(
    map(lambda x, y: x+y, list(map(str, data_label2)), units))

pie2, _ = ax.pie(data2, radius=1,  # 1-width2,
                 labels=labels2, labeldistance=1.1, colors=cin, startangle=90)
plt.setp(pie2, width=width2, edgecolor='white')
labels1.append('Completed Program')
plt.legend(list(labels1), loc='lower left')
plt.title('Program Completion Rate by BWI Program')
# plt.show()

plt.savefig('./graph.png')
