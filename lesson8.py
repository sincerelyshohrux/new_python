# adj=['red','big','tasty']
# fru=['apple','banana','cherry']

# for x in adj:
#     for y in fru:
#         print(x,y)



#while
# son=10
# while son>=1:
#     print(son)
#     son-=1

# i=3
# while i<6:
#     print(i)
#     if i==3:
#         break
#     i+=1


# i=0
# while i<6:
#     i+=1
#     if i ==3:
#         continue
#     print(i)





# i=1
# while i<6:
#     print(i)
#     i+=1
# else:
#     print(' i 6 dan kottalashmedi')



# key='lambo'
# n=2
# while True:
#     answer=input('Parolni ayting:')
#     if answer.lower()==key:
#         print('Xush kelibsan')
#         break
# else:
#     print('Parol notogri')



# import random

# son=random.randint(1, 100)
# marta=0
# while True:
#     user_answer=input('1 dan 100 taxmin qilin(no):')

#     if user_answer=='no':
#         break
#     if int(user_answer)>son:
#         print('Siz oylagandan kichikroq')
#     if marta==5:
#         print(f"son")
#     elif int(user_answer)<son:
#         print('siz oylagandan kattaroq')
# else:
#     print(f"topdingiz {user_answer} kompyuter {son}")
    




# import random
# sides=['left','right','center']
# while True: 
#     gk=random.choice(sides)
#     user_answer=input(f"{sides} lardan biriga tepin:")
#     if user_answer=='no':  
#         break
#     if not user_answer in sides:
#         print(f"faqat{sides} larga tepin")
#         continue                               
#     if user_answer==gk:
#         print('No goal')
#     else:
#         print('goal')



import random
bel=['*','-','+','//']
while True:
    son1=random.randint(1,10)
    son2=random.randint(1,10)
    amal=random.choice(bel)
    misol=f"{son1}{amal}{son2}=?"

    if amal=='+':
        javob=son1+son2
    elif amal=='-':
        javob=son1-son2
    elif amal=='*':
        javob=son1*son2
    elif amal=='//':
        javob=son1//son2

    print(misol)
    user_answer=input('javobingizni yozing:')
    if user_answer=='no':
        break
    if int(user_answer)==javob:
        print(f"javob togri {javob} sizni javob {user_answer}")
    else:
        print(f"xato javob {javob}")











































print('Task1')


grades = [('Ali', 87), ('Vali', 92), ('Sami', 76), ('Gulnoza', 92), ('Madina', 85)]
only_grade = [b for _, b in grades]

yuqori_baho = max(only_grade)
past_baho = min(only_grade)
m = sum(only_grade) / len(only_grade)

yuqori_oquvchi = [ism for ism, grade in grades if grade == yuqori_baho]

print("Barcha baholar:", grades)
print("Eng yuqori baho:", yuqori_baho)
print("Eng past baho:", past_baho)
print("Ortacha baho:", round(m, 1))
print("Eng yuqori bahoga ega oquvchilar:", ", ".join(yuqori_oquvchi))



print('Task2')


ombor = [
    ("Non", 3000),
    ("Sut", 7000),
    ("Go‘sht", 45000),
    ("Shakar", 12000),
    ("Choy", 9000)
]


def narx_ol(mahsulot):
    return mahsulot[1]   


eng_qimmat = max(ombor, key=narx_ol)
eng_arzon = min(ombor, key=narx_ol)

print("Eng qimmat mahsulot:", eng_qimmat[0], "-", eng_qimmat[1])
print("Eng arzon mahsulot:", eng_arzon[0], "-", eng_arzon[1])


def katta_5000(mahsulot):
    return mahsulot[1] > 5000

yuqori_5000 = [nom for nom, narx in ombor if katta_5000((nom, narx))]
print("Narxi 5000 dan yuqori mahsulotlar:", ", ".join(yuqori_5000))


def umumiy_narx(ombor_royxati):
    jami = 0
    for _, narx in ombor_royxati:
        jami += narx
    return jami

print("Barcha mahsulotlarning umumiy narxi:", umumiy_narx(ombor))




print('Task3')
sonlar = [23, -5, 10, 0, -30, 8, 99, -17, 42, 7]
for s in sonlar:
    if s % 2==0:
        print(s, end=" ")
print('Juft sonlar')
 
for x in sonlar:
    if x % 2!=0:
        print(x, end=" ")
print('Toq sonlar')

for m in sonlar:
    if m>0:
        print(m , end=" ")
print('Musbat sonlar')

for m in sonlar:
    if m<0:
        print(m , end=" ")
print('Manfiy sonlar')

eng_katta=max(sonlar)
print('Eng katta son:', eng_katta)
eng_kichik=min(sonlar)
print('Eng kichik son:', eng_kichik)
m=sum(sonlar)/ len(sonlar)
print('Ortacha son:', m)

print('Task4')
words=["dasturlash", "python", "algoritm", "mantiq", "texnologiya"]
eng_uzun=max(words, key=len)
print('Eng uzun soz:', eng_uzun)

print('Har bir sozdagi eng kop bolgan harflar:')
for s in words:
    eng_kop=max(s ,key=s.count)
    print(f"{s}:{eng_kop}")


barcha=' '.join(words)
eng_kop_harf=max(barcha, key=barcha.count)
print('Barcha sozlar orasida eng kop uchraydigon harf:', eng_kop_harf)  


print('Task5')
rooms = {
    101: "band",
    102: "bo'sh",
    103: "band",
    104: "bo'sh",
    105: "band"
}
for xona , x in rooms.items():
    if x=='bosh':
        print(f"Mehmon uchun xona {xona} tayyor!")
        rooms[xona]='band'
        topildi=True
        break

if not topildi:
    print('Kechirasiz, bosh joy yoq')

boshxonalar=[]
for xona , m in rooms.items():
    if m =='bosh':
        boshxonalar.append(xona)
if boshxonalar:
    print('Bosh xonalar:', boshxonalar)
else:
    print('Yoq')

