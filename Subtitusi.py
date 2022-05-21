import os

def clear():
    os.system('cls')


x1 = 8
y1 = 6
n1 = 62

x2 = 2
y2 = 2
n2 = 22

# Mencari Y
a = n2 / x2
b = -y2 / x2
c = (x1*b) + y1
n3 = n1 - (x1*a)
y3 = n3 / c

# Mencari X
d = y2 * y3
n4 = n2 - d
x3 = n4 / x2


clear()
print("Diketahui Persamaan")
print("8x + 6y = 62")
print("2x + 2y = 22")
print("Metode Subtitusi")
print(f"Nilai x dan y adalah x = {x3} dan y = {y3}")
