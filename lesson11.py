# x=10
# print(x)

# def data():
#     global x
#     x=11
#     return x

# print(x)
# new=data()
# print(new)


# def new(a,b,/,*,c,d):
#     print(a+b+c+d)
# new(4,5, c=1,d=10)


# def new(m):
    
#     return 4*m, m**2

# x=new(7)
# print(x)


# def new(m):
#     return m.count('a')
# new('Assalomu aleykum')
# print('a' in new)


# m=20
# salary=[200,800,300,400]

# salary=[s+m for s in salary]
# print(salary)

# m=lambda x:x()
# m=lambda x:x.upper()
# print(m('inha'))

# salary=[200,8009,3001,400]
# data=filter(lambda x:x%2==0, salary)
# print(list(data))



# salary=[200,8009,3001,400]
# answer=list(map(lambda x:x+19,filter(lambda x:x%2==0, salary)))
# print(answer)




# from functools import reduce
# salary=[5,2,3,4]
# answer=reduce(lambda x,y:x/y, salary)
# print(answer)







# m=['olma','banan']
# m=['olma','banan','uzum']
# z=[2000,3000]
# x=list(zip(m,z))
# print(x)

# m=['olma','banan','uzum','okfvd','cbsfx']
# for i



print('Task1')
def total_price(*args):
    return sum(args)
natija=total_price(10,20,30,40.5)
print('Total', natija)

print('Task2')
def update_profil(**kwargs):
    return kwargs
m=update_profil(
    name='ali',
    city='Toshkent',
    age='22'
)

print(m)


# print('Task3')
# def calculate_tax():
#     summa = float(input())
#     stavka= input()
    
#     if stavka == "":
#         stavka = 12                
#     else:
#         stavka = float(stavka)
    
#     tax = summa * stavka / 100
#     print(f"Tax: {tax}")



# calculate_tax()