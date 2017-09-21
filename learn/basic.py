from operator import itemgetter
# name=input('输入你的名字')
# print('您的名字是：',name)
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

print('%.1f'% (72/85))


# 函数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Adam', 45, gender='M', job='Engineer')


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3,4,45))



# 生成器
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L1 if isinstance(x,str)]
print(L2)
g=(x.lower() for x in L1 if isinstance(x,str))
for x in g:
    print(x)


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=itemgetter(1),reverse=False))