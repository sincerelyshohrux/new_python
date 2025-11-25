# new=['olma','anor','behi',[2,3,4,5],{'onix','gentra','byd'},('non','cola','pepsi')]
# # for m in new():
# if 'pepsi' in new[-1]:
#     print('pepsi')


# my_dict={
#     'adres':{
#         "kocha":'bandit',
#         "uy":13,

#     },
#     "hunar":['hal qiluvchi',"rasm chizish",'futbol','pubg']
# }
# if 'rasm chizish' in my_dict[5]:
#     print('rasm chizish')


# yosh=int(input('yoshingizni yozing:'))
# if yosh<13:
#     print('bolalar uchun film')
# elif yosh<18:
#     print('osmirlar uchun film')
# else:
#     print('kattalar uchun film')


# yosh=int(input('yoshingizni yozing:'))
# if yosh%2==0:
#     print('fizz')
# else:
#     print('bizz')


# a=33
# b=200
# if a<b: print("b katta a dan ")




# fru=['apple','banan','chery']
# for x in fru:
#     print(x)
#     if x=="banan":
#         break
  
# fru=['apple','banan','chery']
# for x in fru:
#     if x=='banan':
#         continue
#     print(x)




print('Task1')
num=int(input('Son kiriting:'))
if num > 0:
    print('musbat son')
else:
    print('manfiy son')


print('Task2')
grades=int(input('0 dan 100 gacha son kiriting:'))
if 90<= grades <=100:
    print("A")
elif 80<= grades <=90:
    print("B")
elif 70<= grades <=80:
    print("C")
elif 60<= grades <=70:
    print("D")
else:
    print("F")

print('Task3')
a=int(input('1-nchi sonni kiriting:'))
b=int(input('2-nchi sonni kiriting:'))
c=int(input('3-nchi sonni kiriting:'))
if a>b and a>c:
    print("Eng katta son ", a)
elif b>a and b>c: 
    print("Eng katta son",b)
else:
    print('Eng katta son',c)

print('Task4')
year=int(input('Yilingizni kiriting:'))
if year%4==0 and(year%400==0 or year%100!=0):
    print(year,'kabisa yili' )
else:
    print(year,'kabisa yili emas')

print('Task5')
parol=input('Parolni kiriting:')
if parol=='12345':
    print('xush kelibsiz')
else:
    print('Notori parol')


print('Task6')
m=int(input('Sonni kiriting:'))
if m%3==0 and m%5==0:
    print(m,'3 ga va 5 ga bolinadi')
elif m%3==0:
    print('Faqat 3 ga bolinadi ')
elif m%5==0:
    print('Faqat 5 ga bolinadi')
else:
    print('Hich qaysi songa bolinmedi')

