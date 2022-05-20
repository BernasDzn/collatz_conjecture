#============================================
import matplotlib.pyplot as plt
import numpy as np
#============================================

start_x = 1

while start_x <= 1:
    start_x = int(input("Choose a value for x: "))
cur_x = start_x
val = []
y = []
val.append(cur_x)
n = 0
y.append(0)
xmax = cur_x
while cur_x>1:
    if cur_x%2 == 0:
        cur_x = round(cur_x/2)
    else:
        cur_x = round(3*cur_x+1)
    n=n+1
    val.append(cur_x)
    y.append(n)
    if cur_x > xmax:
        xmax = cur_x

#================== PRINT ===================
print(val)
print(y)
#============================================
#================== PLOT ====================
fig, ax = plt.subplots()
plt.grid(linestyle='--', linewidth=0.5)
ax.plot(y, val, 'o:r')

#============================================
for x,y in zip(y,val):

    label = f"{y}"

    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

#============================================               

plt.show()
#============================================