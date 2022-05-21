import matplotlib.pyplot as plt
   
x = [2.0, 4.2, 6.0]
y = [2.1, 3.2, 4.0]
  
plt.plot(x, y, marker='o')
plt.title('grafik interpolasi')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()