import os

def clear():
    os.system('cls')


x1 = 8
y1 = 6
n1 = 62

x2 = 2
y2 = 2
n2 = 22

a = x2*y2

p = x1 - a * x2
q = y1 - a * y2
r = n1 - a * n2

y3 = r/q
x3 = (y3 * y2 - n2) / -x2

clear()
print("Diketahui Persamaan")
print("8x + 6y = 62")
print("2x + 2y = 22")
print("Metode Eleminasi")
print(f"Nilai x dan y adalah x = {x3} dan y = {y3}")