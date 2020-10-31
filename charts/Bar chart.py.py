import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 6
means_Applications = (90, 78, 40, 89, 76, 56)
means_Selected = (85, 62, 30, 20, 50, 40)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_Applications, bar_width,
alpha=opacity,
color='b',
label='Applications')

rects2 = plt.bar(index + bar_width, means_Selected, bar_width,
alpha=opacity,
color='g',
label='Selected')

plt.xlabel('JOBS')
plt.ylabel('APPLIED/SELECTED')
plt.title('EMPLOYEE RECRUITMENT SYSTEM')
plt.xticks(index + bar_width, ('DEVELOPERS', 'ACCOUNTANT', 'ADMINISTRATION', 
		'DATABASE HANDLER', 'PRODUCT DESIGNERS', 'WORKERS'))
plt.legend()

plt.tight_layout()
plt.show()