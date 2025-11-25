# #tuple va set


davlat=['uzb','amerka','ispaniya','yaponiya','koreya']
print(len(davlat))
print(davlat)

for m in davlat:
    print(m)
sonli=[]
for l in davlat:
    son=len(l)
    sonli.append(son)
print(sonli)

country=['uzb','amerka','ispaniya','yaponiya','koreya']
lesson_tuple=('uzb','amerka','ispaniya','yaponiya','koreya')
country.append('new')
print(country)
print(lesson_tuple)      #tuple da append, remove, del va boshqalar ishlamedi lekin tuple ni listga ozgartirib ishlatsek boladi

lesson_tuple=('uzb','amerka','ispaniya','yaponiya','koreya')
lesson_tuple=list(lesson_tuple)
lesson_tuple.append('new')
print(lesson_tuple)      #tuple ga narsa qoshmoqchi bolsek 1 nchi list ga ozgartiramiz keyin element qoshib yana tuple ga qaytarib qoyamiz


lesson_tuple=tuple(lesson_tuple)
print(lesson_tuple)

new=('olma')
print(type(new))
print(new)         #tuple ichidagi elementdan keyin , qoyish kerak

meva=('banan',)
print(type(meva))
print(meva)
meva=('olma','o;lma',4,4,4,)      #tuple da hamma malumot turlarini ishlatib ketsak boladi va 1 ta element 2 va umdan kop martta ishlatsak boladi
print(meva)

ism='shohrux'
name='shohrux'
print(id(ism))
print(id(name))

cars=['onix','bmw']
old=['onix','bmw']
print(id(cars))
print(id(old))

my_tuple=(10,20,30)
print(my_tuple[0])     #tuple ichidagi elementlarni oqish
print(my_tuple[0:2])     # bolaklab oqish

old_tuple=(1,2,3)
new_tuple=old_tuple+(4,5)    #tuple ni update qilish
print(new_tuple)

new=('olma','banna','nok',['ananas'])
print(id(new))
new[-1].append('anor')
print(new)
print(id(new))       #bunda tupe ozgarmidi faqa ichiga yangi element qoshiladi holos

students = ("Ali",  "Zebo", "Javohir", "Ali", "Zebo", "Ali")
print(students.count('Ali'))

# set

new_set={'non','choy','non'}
print(new_set)

new_set={'non','choy','non',1,True}
new_set={'non','choy','non',True,1}
new_set={'non','choy','non',False,0}
print(new_set)

new_set={'code','choy','non',False,}
new_set.add('coffe')
print(new_set)

print('non' in new_set)


new_set={'code','choy','non','banana'}
new_set.discard('choy')
# new_set.remove('code')
print(new_set)b=[3,4,5,6]


new_set={'code','choy','non','banana'}
new_set.clear()
print(new_set)

#union (birlashtirish)
a={1,2,3}
b={3,4,5}
print(a.union(b))

#intersection (2 kala setdan umumiy elementlarni olish)
a={1,2,3}
b={3,4,5}
print(a.intersection(b))

#difference ( 1 nchi setdagi lekin 2 nchi setda yo elementlarni olish)
a={1,2,3}
b={2,3,4}
print(a.difference(b))



#simmetric_difference (ikkala setdan faqat 1 tada bolgan elementlarni olish)
a={1,2,3}
b={3,4,5}
print(a.symmetric_difference(b))

print('Task1')
nums=[1,2,3,2,4,1,5]
unique_numbers=list(set(nums))
print(unique_numbers )

print('Task2')
a=[1,2,3,4]
b=[3,4,5,6]
a=set(a)
b=set(b)
print(a.intersection(b))


print('Task3')
a=[1,2,3,4]
b=[3,4,5,6]
a=set(a)
b=set(b)
print(a.difference(b))


print('Task4')
a=[1,2,2,3,4,4,5]
a=set(a)
print(len(a))

print('task5')
n=int(input("so'zlar sonini kiriting:"))
soz=[]
for l in range(n):
    m=input(f"{l+1} so'zni kiriting:")
    soz.append(m)
unique_soz=set(soz)
print(f"Unikal so'zlar soni: {len(unique_soz)}")

print('Task6')
text=('hello world')
for m in text:
    if m.isalpha():
        print(m)

text='hello world'
new=set()
for t in text:
    new.add(t)
print(new)
