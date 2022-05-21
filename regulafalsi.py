a = 1.0 #batas bawah
b = 6.0 #batas batas
n = 7 #batas iterasi
fa = 2*a**3+2*a**2-a+2
fb = 2*b**3+2*b**2-b+2


for i in range (1,n+1):
    x = b - ((fb)/(fb-fa))*(b-a)
    fx = 2*x**3+2*x**2-x+2
    if abs(fa) < 1.0e-8:
        break
    elif fa*fx < 0:
        b=x
        fb = fx
    else:
        a=x
        fa = fx
        
print("Akar penyelesaian yang didapat adalah x = %.3f dengan nilai f(x) = %.3f" % (x,fx))