import sys
#import english
#import matplotlib.pyplot as plt
import hashlib
#import numpy as np
#import matplotlib.pyplot as plt

#/ get all lines from stdin, remove leading and trailing whitespace and split the line into words
file = open("english", "r")
x_val = []
y_val = []
px_val = []
py_val = []
for line in file:
    line = line.strip()
    line = line.split()

    # output tuples [word, 1] in tab-delimited format
    i=0;
    for word in line:
        if i % 2 == 0:
            i += 1
            py_val.append(int(word))
        else:
            px_val.append(int(word))
print('X:', px_val,
      "\n Y: ", py_val)


max_x = max(px_val)
max_y = max(py_val)
print ("Max X: ", max_x)
print ("Max Y: ", max_y)


for val in px_val:
    new_val = val/max_x
    x_val.append(new_val)
for val in py_val:
    new_val = val/max_y
    y_val.append(new_val)
print(x_val)
print(y_val)





        #print('%s\t%s' % ((word), "1"))



