import math
print('\tcalculator\t')
print("**************************")
print("1.Add\n2.Subract\n3.Multiply\n4.Divide\n5.Square\n6.Sqaure root\n7.Exponent\n8.Log\n9.Anti log\n10.Exit")

while True:
  num = input("Write the respective number of the function to perform: ")

  if num == '10':
    break
  if num == '1':
    x =  float(input("enter the number to add: "))
    y = float(input("enter the number to add: "))
    print(x+y)
  elif num == '2':
     a = float(input("Enter the number to subtract: "))
     b = float(input("Enter the number to subtracr: "))
     print(a-b)

  elif num == '3':
    c = float(input("enter the number to be multiplied: "))
    d = float(input("enter the number to be multiplied: "))
    print(c*d)
  elif num == '4':
    e = float(input("enter the dividend: "))
    f = float(input("enter the divisor: "))
    print(e/f)
  elif num == '5':
    g = float(input("enter the number whose sqaure is to be found: "))
    print(g*g)
  elif num == '6':
    h = float(input("enter the number whose square root is to be found: "))
    print(math.sqrt(h))
  elif num == '7':
    j = float(input("enter te number: "))
    k = float(input("enter the power: "))
    print(j**k)
  elif num == '8':
    i = float(input("enter the number whose log to natural base is to be found: "))
    print(math.log(i))
  elif num == '9':
    l = float(input("enter the number whose antilog is to be found: "))
    print(math.exp(l))
