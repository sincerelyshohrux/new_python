# ## def
# def salom():
#     print(f"Assalomi aleykum")
# salom()

# def salom(name):
#     print(f"assalomu aleykum  {name}")
# salom('ali')
# salom('shoh')



# def hisoblash(x,y):
#     if x>y:
#         print(x)
#     elif x==y:
#         print('=')
#     else:
#         print(y)
# hisoblash(x=209,y=-2122)


# def answer(x,y):
#     if x>y:
#         print(x)
#     elif x==y:
#         print('=')
#     else:
#         print(y)
    
    

# def m(ism,age):
#     year=2025
#     new=f"ism:{ism} yoshi{year-age}"
#     print(new)

# m('shohrux', 18)
# m(ism='shohrux', age=18)


# def num(x):         # darajaga oshirish
#     print(x**3)
# num(5)
# num(4)
# num(2)
    

print('Task1')
def num(x):

    if x % 2==0:
        print('Juft son')
    else:
        print('Toq son')
    
num(5)
num(88)
num(-12)

print('Task2')
def ism(name):
    print(f'Salom {name}')
ism('Shohruh')


print('Task3')

def answer(x,y):
    return x+y 
x=answer( 3,10)
print(x)


print('Task4')
def m(a):
    print(a**2)
m(6)

    
print('Task5')
n=int(input('Yoshingizni yozing:'))
def name(x):
    if x>18:
        print('Sizni yoshingiz 18 dan katta')
    else:
        print('Yoshingiz 18 da kichik')
        
name(n)
    


print('Task6')
def num(a,b,c):
    return a*b*c
c=num(2,3,6)
print(c)

        
print('Task7')
def matn(x):
    return x[::-1]
m=matn('Stringni teskari yozish')
print(m)


print('Task8')
def num(a,b,c):
    return max(a,b,c)
a=int(input('1-nchi sonni kiriting:'))
b=int(input('2-nchi sonni kiriting:'))
c=int(input('3-nchi sonni kiriting:'))
print('Eng katta son', num(a,b,c))


print('Task10')
def m(a, b):
    return (a+' '+b)
a='Inha'
b='university'
print(m(a,b))









