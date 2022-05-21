# Linear interpolation in python

# Input section
# Reading first point
x0 = 2.0
y0 = 2.10

# Reading second point
x1 = 6
y1 = 4.10

# Reading calculation point
xp = 4.2

# Calculating interpolated value
yp = y0 + ((y1-y0)/(x1-x0)) * (xp - x0)

# Displaying result
print('Interpolated value at %0.1f is %0.1f' %(xp,yp))