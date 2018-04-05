# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt


N = 5 #Number of columns
level_1_name = "Freddy Mc'Fredson" #These dictate the bar names.
level_2_name = "Kelly Kentucky" #These dictate the bar names.
level_1_values = (20, 35, 30, 35, 27) #Changes the height of the level_1 bars
level_2_values = (25, 32, 34, 20, 25) #Changes the height of the level_2 bars

ind = np.arange(N)    # the x locations for the groups
width = 0.35 # Change the width of the bars

p1 = plt.bar(ind, level_1_values, width, color='pink')
p2 = plt.bar(ind, level_2_values, width, color='purple', bottom=level_1_values)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))

plt.legend((p1[0], p2[0]), (level_1_name, level_2_name)) 

plt.show()
