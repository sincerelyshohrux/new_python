# print('Hello world')

# a=2
# b=5
# # if a<b:
# #     print('5 2 dan katta' )
# # else:
# #     print('2 5 dan kichik')
# print(type(a))

# # a=2; b=7
# print(a+b)
# age='20'
# home='15'
# print(age+home)
# print(age+' '+home)
# print(type(age))

# x=5
# y='python'
# print(x)
# print(y)

# x=5
# x='salom'
# x=3
# x='salom'
# x='dunyo'
# print(x)

# x,y,z='olma','nok','banan'
# print(x)
# print(y)
# print(z)

# x='university'
# print('inha'+' '+x)

# x='inha'
# y='toshkent'
# print(x+y)
# print(y+' '+x)


# x=5
# x+=2
# print(x)

# x=5
# y=12
# print(x+y)

# x='qiziq'
# def funksiya():
#     print('dasturlash juda'+ ' '+x)
# funksiya()

# y='qozon'
# def function ():
#     print(' yunsobod Besh'+ ' '+y)
# function()

# x='shirin'
# def funksiya ():
#     x='foydali'
#     print('olma'+' '+x)
# funksiya()
# print('olma'+' '+x)



# def funksiya():
#     global x
#     x='shirin'
#     print('olma'+' '+x)
# funksiya()
# print('olma'+' '+x)



## mantiq operatorlari
# a=6
# print(a<3 and a>2 ) 
# print(a<7 or a==5)
# print (not(a<3 or a>10)) 
# print (not(a>2 or a==4))  


  

    ## aniqlash opetatorlari
# x=['olma','banan']
# y=['olma','banan']
# z=x
# x=2
# y=5
# z=x
# print(x is z)
# print(x is y)
#  print(x == z)  

# print(x is not z)     
# print(x is not y)    
# print(x != z)  

# azolik operatorlari
# x=('audi','mustang')
# print('audi'in x)
# print('mustang' not in x)


# int
# x=1
# print(type(x))


# for m in range(1000000):
#     print('Men maftuna ni yaxshi koraman')

## complex
# x=complex(1,9)
# print(x)

# x=1
# a=float(x)
# b=complex(x)
# print(a)
# print(b)

## random modul
# import random
# print(random.randrange(1,10))

# narx=30
# satr='Mahsulot narxi {} som'
# print(satr.format(narx))

# sana=5
# oy='avgust'
# yil=2007
# bugun='Bugun {} - {},{} -yil'
# print(bugun.format(sana, oy, yil))


# soat=3
# fan='OOP'
# dars='Bugun {0} soat darsimiz bor. Darsimiz {1}'
# print(dars.format(soat, fan))

# satr='Uning ismi {ism}, yoshi {yosh} da'
# print(satr.format(ism='Shohruxbek ', yosh=180))


# ##list
# meva=list(('olma','banan','nok'))
# print(meva)

# car=['Bmw','audi','rr']
# print(car[1])
# print(car[-1])

# meva = ["olma", "banan", "apelsin", "nok", "uzum"]
# print(meva[0:2])
# print(meva[:4])
# print(meva[0:])

# meva = ["olma", "banan", "apelsin", "nok", "uzum"]
# meva[0]='anor'
# print(meva)


# car = ["Audi", "Mustang", "Ferrari"]
# for x in car:
#     print(x)
#     print(x.upper())

# salon= ["Audi", "Mustang", "Ferrari"]
# if 'Audi' in salon:
#     print('Audi bor')
# else:
#     print('Audi yoq, mustang bor')



# meva1= ["olma", "banan", "apelsin", "nok", "uzum"]
# meva2=meva1.copy()
#print(meva2)

# meva2=list(meva1)
# print(meva2)

# a = [1, 2, 3, 4, 5]
# b = [5, 6, 7]
# c= a + b
# print(c)
# a+=b
# print(a)


# mashina1 = ["Audi", "Mustang", "Ferrari"]
# mashina2 = ["BMW", "mercedes", "Porsche"]
# for x in mashina2:
#     mashina1.append(mashina2)

# print(mashina1)

# a=[1,2,3,4,5,5,2,4,2]
# x=a.count(2)
# print(x)
# x=a.index(5)
# print(x)


# ## sortlash
# meva = ["olma", "banan", "apelsin", "nok", "uzum"]
# a = [1, 2, 5, 4, 3]
# meva.sort()
# print(meva)
# a.sort()
# print(a)


# ## manfiy indeks
# a = ("kitob", "daftar", "ruchka")
# print(a[-1])

# ## indeks oraligi
# a = ("kitob", "daftar", "ruchka", "qog'oz", "qalam")
# print(a[0:3])


# ##Element qiymatlarini o’zgartirish
# a = ("kitob", "daftar", "ruchka")
# b=list(a)
# b[1]='qalam'
# print(b)


# a = ("kitob", "daftar", "ruchka")
# for n in a:
#     print(n)

# if  'qalam' in a:
#     print('Bizda qalam bor')
# else:
#     print('Bizda qalam yoq  ')

# tuple
# a = ("kitob", "daftar", "ruchka")
# b = ("qalam", "qog'oz")
# c=a+b
# a+=b
# print(c)
# print(a)


toq_son = (1, 3, 5, 3, 3, 7)
x=toq_son.count()
print(x)







