import math as mth
print("Mark II, version 1.50.2")
print("Made and coded by Rutheford")

print ("What would you like to do, man? Plant a Tree, calculate the sqrt of Pi?...")
A= float(input("FIRST number:"))
B= float(input("Another number:"))
Plus = A + B
print ("Result A + B=", Plus)
Minus= float(input("Number to do the subtraction:"))
print("New answer=", Plus - Minus)
Y = Plus - Minus
multiplication = float(input("Number to multiply:"))
print ("multiplication answer=",Y * multiplication)
Z = Y * multiplication
Division = float(input("Put the number to divide"))
print (f"Division has this result= {Z}/{Division}")
DecimalDivision = print (f"The exact division has this result= {Z}//{Division}")
Module = float(input("Module number "))
print (f"Answer of the module= 1 %({Z}/{Division})")
V = Z/Division
Exponential = float(input("Number to the power of")) 
print ("Result of power=", V** Exponential)
G = V** Exponential
squareratea = print ("Answer=", G**(1/2))
squarerateB = mth.sqrt(B)
print ("Your Square rate=", squarerateB)


print ("Loading binary/Octal/hexadecimal mode:")
print ("Binary/octal/hexadecimal mode. Version 1.0")
b= int(input("Numeric base (2,8,16): "))
x1=int(input("digito boh: "))
if x1 >15 :
    exit()
if b == 2 and x1 >1:
 exit()  
if b == 8 and x1 >8:
   exit()  
x2= int(input("number boh: "))
if x2 > 15:
    exit()
if b == 2 and x2 >1:
 exit()
if b == 8 and x2 >8:
   exit()  
x3= int(input("number boh: "))
if x3 > 15:
    exit()
if b == 8 and x3 >8:
   exit()  
if b == 2 and x3 >1:
 exit()  
x4= int(input("number boh: "))
if x4 > 15:
    exit()
if b == 2 and x4 >1:
 exit()
if b == 8 and x4 >8:
   exit()         
x5= int(input("number boh: "))
if x5 > 15:
    exit()
if b == 2 and x5 >1:
 exit()
if b == 8 and x5 >8:
   exit()    
x6= int(input("number boh: "))
if x6 > 15:
    exit()
if b == 8 and x6 >8:
   exit()  
if b == 2 and x6 >1:
 exit()  
x7= int(input("number boh: "))
if x7 > 15:
    exit()
if b == 2 and x7 >1:
 exit()
if b == 8 and x7 >8:
   exit()     
x8= int(input("number boh: "))
if x8 > 15 :
    exit()
if b == 2 and x8 >1:
    exit()
if b == 8 and x8 >8:
   exit()    
x9= int(input("number boh: "))
if x9 >15:
    exit()
if b == 8 and x9 >8:
   exit()  
if b == 2 and x9 >1:
 exit()   
x10= int(input("number boh: "))
if x10 > 15:
    exit()
if b == 2 and x10 >1:
    exit()
if b == 8 and x10 >8:
   exit()        
x11= int(input("number boh: "))
if x11 > 15:
 exit()
if b == 2 and x11 >1:
 exit()
if b == 8 and x11 >8:
   exit()    
x12= int(input("number boh: "))
if x12 > 15:
 exit()
if b == 2 and x12 >1:
 exit()
if b == 8 and x12 >8:
   exit()    
X=x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12
Total= ('answer')
Total = (mth.pow(b,12-1)*x1) +(mth.pow(b,12-2) *x2)+(mth.pow(b,12-3) *x3)+(mth.pow(b,12-4) *x4)+(mth.pow(b,12-5) *x5)+(mth.pow(b,12-6) *x6)+(mth.pow(b,12-7) *x7)+(mth.pow(b,12-8) *x8)+(mth.pow(b,12-9) *x9)+(mth.pow(b,12-10) *x10)+(mth.pow(b,12-11) *x11)+(mth.pow(b,12-12) *x12)
print (f"Your number:{Total}, in base 10. Orignally, it were in the base of {b}, as {X}")

print ("Preparando modo binário/Octal/hexadecimal:")
print ("Modo binário/octal/hexadecimal. Version 1.0")
b= int(input("Escolha a base numérica (2,8,16): "))
x1=int(input("digito boh: "))
if x1 >15 :
    exit()
if b == 2 and x1 >1:
 exit()  
if b == 8 and x1 >8:
   exit()  
x2= int(input("digito boh: "))
if x2 > 15:
    exit()
if b == 2 and x2 >1:
 exit()
if b == 8 and x2 >8:
   exit()  
x3= int(input("digito boh: "))
if x3 > 15:
    exit()
if b == 8 and x3 >8:
   exit()  
if b == 2 and x3 >1:
 exit()  
x4= int(input("digito boh: "))
if x4 > 15:
    exit()
if b == 2 and x4 >1:
 exit()
if b == 8 and x4 >8:
   exit()         
x5= int(input("digito boh: "))
if x5 > 15:
    exit()
if b == 2 and x5 >1:
 exit()
if b == 8 and x5 >8:
   exit()    
x6= int(input("digito boh: "))
if x6 > 15:
    exit()
if b == 8 and x6 >8:
   exit()  
if b == 2 and x6 >1:
 exit()  
x7= int(input("digito boh: "))
if x7 > 15:
    exit()
if b == 2 and x7 >1:
 exit()
if b == 8 and x7 >8:
   exit()     
x8= int(input("digito boh: "))
if x8 > 15 :
    exit()
if b == 2 and x8 >1:
    exit()
if b == 8 and x8 >8:
   exit()    
x9= int(input("digito boh: "))
if x9 >15:
    exit()
if b == 8 and x9 >8:
   exit()  
if b == 2 and x9 >1:
 exit()   
x10= int(input("digito boh: "))
if x10 > 15:
    exit()
if b == 2 and x10 >1:
    exit()
if b == 8 and x10 >8:
   exit()        
x11= int(input("digito boh: "))
if x11 > 15:
 exit()
if b == 2 and x11 >1:
 exit()
if b == 8 and x11 >8:
   exit()    
x12= int(input("digito boh: "))
if x12 > 15:
 exit()
if b == 2 and x12 >1:
 exit()
if b == 8 and x12 >8:
   exit()    
X=x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12
Total= ('resposta')
Total = (mth.pow(b,12-1)*x1) +(mth.pow(b,12-2) *x2)+(mth.pow(b,12-3) *x3)+(mth.pow(b,12-4) *x4)+(mth.pow(b,12-5) *x5)+(mth.pow(b,12-6) *x6)+(mth.pow(b,12-7) *x7)+(mth.pow(b,12-8) *x8)+(mth.pow(b,12-9) *x9)+(mth.pow(b,12-10) *x10)+(mth.pow(b,12-11) *x11)+(mth.pow(b,12-12) *x12)
print (f"Aqui está seu número:{Total}, em base 10. Originalmente estava na base {b}, como {X}")
