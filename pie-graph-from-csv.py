import matplotlib.pyplot as plt
import csv

"""
We have 3 elements to a pie graph that we need to populate.

Elements
--------
labels: 
    Labels describe the names for the pie slices and are rendered on the
    outermost perimeter.
Sizes:
    The sizes variable dictates the percentage split of the graph. 
    NOTE* These must add up to 100 percent.
Explode:
    Explode seperates certain slices of the graph and shifts them away
    from the remaining slices. The default value for explode is 0.

Note: Labels and Sized must have the same amount of entries. If you don't want
to have labels for a slice, replace the element with and empty string. E.G.
("")
"""

file_dir = ""
csv_file = open(file_fire, "r")
reader = csv.reader(csv_file, delimeter=',')
for row in reader:
    print(row)
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.5, 0, 0) #Change these values. What does this do to the graph?

fig1, ax1 = plt.subplots() #Creates the pie graph
ax1.set_color_cycle(['pink','blue','yellow','red']) #Change or add more colours 
"""
set_color_cycle allows us to set custom colours for the pie graph. There is no
minimum and their is no limit to the amount of colours specified but if their
are more slices than there are colors defined, they will be reused. To add more
colours, simply follow the syntax above.
"""
ax1.pie(sizes, 
        explode=explode, 
        labels=labels, 
        autopct='%1.1f%%',
        shadow=True, 
        startangle=0) #startangle rotates the whole graph.
ax1.axis('equal')  

plt.show()
