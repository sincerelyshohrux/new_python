# takrorlash

meva=['olma','banan']
cars=['bmw','cobalt']
meva.extend(cars)
print(meva+cars)
print(meva)

##sort  yani elementlarni saralash
cars=['onix', 'bmw','nissan','damas','nexia']
cars.sort()
cars.sort(reverse=True)
print(cars)
n=[1,3,5,356,743,9,7]
n.sort()
n.sort(reverse=True)         
print(n)

# nusxa olish
cars=['onix', 'bmw','nissan','damas','nexia']
nusxa=cars[:]
nusxa=cars.copy()
cars.append("nissan")
print(cars)
print(nusxa)

from copy import deepcopy

cars=['onix', 'bmw','nissan','damas','nexia',['mers','lambo']]
new=deepcopy(cars)
cars[-1].append('nexia')
print(cars)
print(new)



cars=['onix', 'bmw','nissan','damas','nexia']
for m in cars:
    print(m)
    print(m.upper(),'salom')

for x in cars:
    if x=='damas':
        print(x.upper())
    else:
        print(x.lower())



num=int(input("qancha mahsulot kerak:"))
new=[]
for m in range(num):
    answer=input(f"{m+1}-mahsulot nomini yozing: ")
    new.append(answer)
    print(new)
print(new)

korzinka=['sir','sut','banan','cola','pepsi']
for kerak in korzinka:
    if kerak in korzinka:
        answer=f"{kerak} mahsulot bizda bor"
        print(answer)
    else:
        answer=f"{kerak} mhasulot bizda yo'q"
        print(answer)




print("Task1")
list=[3,7,2,5,9]
farq=max(list)-min(list)
print(farq)

print('Task2')
nums=[1,2,3,4,5,6]
juft=[]
toq=[]

for x in nums:
    if x %2 ==0:
        juft.append(x)
    else:
        toq.append(x)

print("juft:", juft)
print("toq:", toq)

print('Task3')
a=3; b=4; c=5
if a+b >c  and a+c >b and b+c>a:
    print('Uchburchak yasash mumkin')
else:
    print('Uchburchak yasash mukin emas')

print('Task4')
fruit=('apple','banana','kiwi','watermelon')
longest=max(fruit, key=len)
print("eng Uzun soz:" , longest)

print('Task5')

baxo=int(input('Bahoni kiritish:'))
if 90<= baxo <=100:
    natija='A'

elif 80<= baxo <=90:
    natija='B'

elif 70<= baxo <=80:
    natija='C'
elif 60<= baxo <=70:
    natija='D'
else:
    natija='F'

print("Baholash natijasi:", natija)
