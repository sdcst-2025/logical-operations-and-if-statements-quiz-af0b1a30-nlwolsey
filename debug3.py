#!python3
"""
Debug this program so that it runs

program should read a float value
and use it as an exponent rounded to 2 decimal places

original code:
x = Input("enter a float number:")
round(x)
print(x)
"""

x = float(input("enter a float number:"))
x2 = x**2
x3 = round(x2,2)
print(x3)