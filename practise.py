# num=[1,2,3,4]
# i=0
# for a in num:
#     for b in num:
#         for c in num:
#             if(a!=b) and (b!=c) and (c!=a):
#                 i+=1
#                 print(a,b,c)
# print('all',i)
#################################################1

# a=[1,3,5,2,4,5,7]
# n=len(a)
# for i in range(0,n):
#     for j in range(i,n):
#         if(a[i]>a[j]):
#             tmp=a[i]
#             a[i]=a[j]
#             a[j]=tmp
# print(a)#冒泡排序
########################################
# a=[1,3,5,2,4,5,7]
# print('正序:{}'.format(sorted(a)))
# print('逆序:{}'.format(list(reversed(sorted(a)))))
######################################
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
# print(fib(4))
# ###################################
# a=[1,2,3,4]
# b=[i for i in a]
# print(b)
# ###############################
# for i in range(1,10):
#     print()
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(i,j,i*j))
# ###################
# import time
# print(time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time())))

###############################
# score=int(input('输入分数：\n'))
# if score >= 90:
#     grade = 'A'
# elif score >= 60:
#     grade = 'B'
# else:
#     grade = 'C'
# print('%d属于%s'%(score,grade))
#########################
# import string
# word=input('输入：\n')
# letter=0
# a=0
# space=0
# others=0
# for c in word:
#     if c.isalpha():
#         letter+=1
#
#     elif c.isspace():
#         space+=1
#     elif c.isnumeric():
#         a += 1
#     else:
#         others+=1
# print('letter=%d,space=%d,others=%d,a=%d'%(letter,a,space,others))#有毒不对

#################
# from functools import reduce
# t=0
# sn=[]
# n=int(input('n='))
# a=int(input('a='))
# for c in range(n):
#     t=t+a
#     a=a*10
#     sn.append(t)
# sn=reduce(lambda x,y:x+y,sn)
# print(sn)
#########################
# a=2
# b=1
# s=0
# for n in range(1,20):
#     s+=b/a
#     t=a
#     a=a+b
#     b=t
# print(s)
###########################实例24
s=0
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
for i in range(1,21):
    a=fact(i)
    s=s+a
print(s)
######################


