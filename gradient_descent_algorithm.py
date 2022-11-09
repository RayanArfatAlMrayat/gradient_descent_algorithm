""" calculate the gradient descent
Rayan arafat AL Mrayat
"""
import sympy
import random
#function x^2+5
def fun(x):
    return ((x**2)+5)
#derivative
def div(m):
    #function
    f = fun(x)
    #calculate the derivative with respect to x
    div_f=f.diff(x)
    # calculate the derivative with respect to m[specific value]
    f2=sympy.lambdify(x,div_f)
    return f2(m)
#assigning a random value to weight
w0=random.randint(0,10)
x=sympy.Symbol('x')
error=1
#print(div(2))
#epsilon =0.009
while error>0.009:
    #change the  weight valu
    # eta =0.04
    w1=w0-(0.04*div(w0))
    # calculate the error/loss
    error=abs(fun(w1)-fun(w0))
    print("old weight value",w0,"new weight value",w1,'error/loss',error)
    w0=w1
print('optimal weight',w0)
#print(div_f)
