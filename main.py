import numpy as np

##### Part 1

dtype1 = np.dtype([('direction', 'U1'), ('value', 'i')])
sweeps = np.loadtxt('input.txt', dtype=dtype1, usecols=(0,1))

horizontal = 0
depth = 0

for i,change in enumerate(sweeps):
    if change['direction'] == 'd':
        depth = depth + change['value']
    if change['direction'] == 'u':
        depth = depth - change['value']
    if change['direction'] == 'f':
        horizontal = horizontal + change['value']
    
print("Final Horizontal: ", horizontal)
print("Final Depth: ", depth)
finLoc = depth*horizontal
print("Final Location: ", finLoc)


##### Part 2

horizontal = 0
depth = 0
aim = 0

for i,change in enumerate(sweeps):
    if change['direction'] == 'd':
        aim = aim + change['value']
    if change['direction'] == 'u':
        aim = aim - change['value']
    if change['direction'] == 'f':
        horizontal = horizontal + change['value']
        depth = depth + aim * change['value']

print("Final Horizontal: ", horizontal)
print("Final Depth: ", depth)
finLoc = depth*horizontal
print("Final Location: ", finLoc)     