str, int,float

a=12
a=a+2
# a=a/3
# a+=12
# a*=5
print(a)

name='ali'
ism='valo'
print(name==ism)
print(name!=ism)  

a=12
b=6
# print(a>b)
print(a==b and a<b)
print(a>b and a==12)    # and uchun ikkala taraf ham true bolsa jabob true chiqadi
print(a>b or a<b)       # or uchun 1 ta true yetarlik

a=4
b=1       
c=3      
d=5    
print(b>a or (c>d and d==3) or (c<b or b==d) and a<c)

matn="assalomu aleykum"
print(matn.replace('a','o'))     # replace yani 1 ta harifni boshqa harifga ozgartirish
age='21'
yosh='11'
print(age+yosh)
print(age+' '+yosh)

matn='lakcmwvh'
matn='ldvv13234'
matn="4563456"
print(matn.isdigit())      #faqat sondan iboratmi
print(matn.isalpha())       # faqat harifdan iboratmi
print(matn.isalnum())         #harf yoki sondan
name=input("ismingizni yozing:")
if name.isalpha():
    print(name)
else:
    print("nma sen qirolmiding!:")





# list    list=[] or list
new='mers'
cars=['nexia','damas', 'byd', 'mbw', new]
print(cars)
print(len(cars))
meva=[]

cars=['nexia','damas', 'byd', 'mbw', 'khg', 'rdckt']
print(cars[1])
print(cars[1:3])
print(cars[:3])
print(cars[:: -1])                 #hammasi hohlagan joydagi narsani korsatib berish

print(cars[0][3])
print(cars[-3][1])           # bular list ichidagi moshinalarni harifini olish uchun ishlatiladi
print(cars[0][4])
print(cars[3][1])
mashina=cars[1]
print(mashina)
cars.append('tico')   # append 1 tadan qoshadi
print(cars)
cars.insert(3,'x7') # insert 3 ni orniga qoshish
cars.insert(2,'lambo')
print(cars)


print(type(cars))
fron=['olma','adcsdc','ascasc','wdqwd']
# cars.extend(fron)
cars+=fron
print(cars)

# remove
cars.remove('byd')
print(cars)

del cars[1]
del cars[0:2]
print(cars)

cars.clear()
print(cars)

#pop      orqa tomondan boshlab 1 tadan ochirish
cars.pop()
cars.pop()
print(cars)

salom=cars.pop()
print(cars)
print(salom)

salon=[]
salon.append(cars.pop())
salon.append(cars.pop())
print(cars)
print(salon)

numbers=[1,2,3,4,5,6,7,8,9]
print(sum(numbers)) 
print(max(numbers))
print(min(numbers))
print(sum(numbers)//len(numbers))

# homework
homework='Task1'
print(homework)
new=['1','2','3']
new.append('4')
print(new)

homework='Task2'
print(homework)
num=['5','10','15','20']
num.remove('15')
print(num)

homework='Task3'
print(homework)
inha=['8','9','10']
inha.remove('9')
inha.insert(1, 99)
print(inha)

homework='Task4'
print(homework)
sum=['1','2','3','4','5']
sum.clear()
print(sum)


homework='Task5'
print(homework)
num=['3','6','9']
num.append('12')
num.append('15')
print(num)


homework='Task6'
print(homework)
m=['7','14','21','28','35']
m.remove('28')
print(m)


homework='Task7'
print(homework)
x=['2','4','6']
x.insert(1,'3')
print(x)


homework='Task8'
print(homework)
o=['1','2','3','4','5']
del o[1:4]
o.insert(1,7)
o.insert(2, 8)
print(o)


homework='Task9'
print(homework)
list=['33','22' ,'11']
new_list=[]
new_list.append(list.pop())
new_list.append(list.pop())
new_list.append(list.pop())
print(list)
print(new_list)


homework='Task10'
print(homework)
a=['4','5','6']
a.pop()
print(a)


homework='Task11'
print(homework)
b=['1','2','3','4','5']
print(len(b))

homework='Task12'
print(homework)
list1=['4','4','6']
list2=['8','10','12']
list1+=list2
print(list1)

homework='Task13'
print(homework)
k=[5,10,15]
son=int(input("sonni yozing:"))
if son in k:
    print(True)
else:
    print(False)

homework='Task14'
print(homework)
n=['7','7','7','3','3']
answer=n.count('7')
print(answer)

homework='Task15'
print(homework)
q=[10,20,30]
answer=q.copy()
print(answer)





