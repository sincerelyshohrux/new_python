#dict
my_dict={}
print(my_dict)
print(type(my_dict))
name='abdullo'

new={
    'name':'shohrux',
    'age':17,
    'shohrux':'andijon',
    'name':name
}
print(new)
print(new['age'])
print(new['shohrux'])



phone={
    'brend':'apple',
    'car':'malibu',
    'price':1200

}
print(phone)

moshina=phone['car']
print(phone)
print(moshina)
print(moshina.upper())

print(phone.get('brend'))           #get bkeyni oladi, bolmasa biz yozgan qiymatni chiqaradi
print(phone.get('brends'))
print(phone.get('brends', 'bunday key yoq'))




phone={
    'brend':'apple',
    'car':'malibu',
    'price':1200
}
print(phone['car'])

new=list(phone.keys())         # keynilist ichiga solish
old=list(phone.values())       # value ni list ichiga solish
jami=list(phone.items())       # item key va value ni birga chiqaradi
print(new)
print(old)
print(jami)
print(jami[-1][0])



car=dict(name='ali', age=20)    # dick ni bunaqa qilib yozib bomidi chunki bunday holatda faqat 1 xil key boladi
print(car)




fruit={             # dict ga yangi element qoshish
    'olma':2000,
    'banan':'sariq',
    'nok':'andijon'
}
fruit['anor']=100
print(fruit)
fruit.update({'new':'old'})
print(fruit)


       #dict ichidagi elementlarni ochirish
phone={              
    'brend':'apple',
    'car':'malibu',
    'price':1200
}
del phone['car']
phone.pop('car')
print(phone)

new=phone.pop('brend') # bunda value new file ga otadi
print(new)

old=phone.popitem()       #dict ni ochirish


phone={              
    'brend':'apple',
    'car':'malibu',
    'price':1200
}
for m in phone:
    print(m,phone[m])


phone={              
    'brend':'apple',
    'car':'malibu',
    'price':1200
}
for m in phone.keys():      # key larni korish
    print(m)

for v in phone.values():   # value ni korish
    print(v)

for k,v in phone.items():    # key bilan value ni birga korish
    print(k,v)

for k,v in phone.items(): 
    print(f"{k}:{v}")


# son=int(input('nechta mahsulot kerak:'))

# new=[]
# for s in range(son):
#     mahsulot=input(f"{s+1} mahsulot yozing:")
#     new.append(mahsulot)



# homework
print("Task1")
students={}
for x in range(2):
    name=input('ismingizni kiriting:')
    age=int(input('yoshingizni yozing:'))
    students[name]=age
print('Natija:', students)


print("Task2")
grades={'Shohrux':[1,2,3], 'Ali':[3,4,5], 'Abdullo':[9,7,8]}
for key, marks in grades.items():
     m=sum(marks) / len(marks) 
print(f"{key} ning ortacha bahosi:{m}")


person={
    'Name':'Shohrux',
    'Age':17,
    'city':'Toshkent'
}
if 'age' in person:
    'age'+=1
print(person)