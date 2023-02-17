import requests 
from bs4 import BeautifulStoneSoup
import selenium
import hashlib
from locale import getdefaultlocale
# a=0
# def cadg(cc,bb = 'zxcv',aa='ff'):
#     print(cc,bb,aa)
r = requests.get("https://www.google.com",verify=False)
print(r.status_code)
# '''cadg('self',aa='我好帥')'''

# def math(x,t,*,z):
#     print(x,t,z)
# '''math(1,2,z=3)'''

# def myfunc(*arg,**args): 
#     print("{}個參數".format(len(arg)))
#     print("第2個是{}".format(arg[1]))
#     print(arg,args)

# '''my = (1,2,3,4,5)'''
# x=4
# def myfuna(s,vt,o):

#     return "".join((o,vt,s))
# '''print(myfuna('你',o='好',vt='屋'))'''
# v=123
# def funxx(): 
#     v=127
#     def funx ():
#         nonlocal v
#         v=12
#         print(v)
#     funx()
#     print(v)
# funxx()
# class hee:
#     def funa(ccc):
#         def funb(aaa):
#             return ccc**aaa
#         return funb
# test = funa(6)
# print(test(3))
# text = 'ttta'
# hash = hashlib.sha3_512(text.encode())
# hashh = hash.hexdigest()
# print(hashh)
# def xxx (cc):
#     cc=cc%2
#     print(cc)
# num = [22,33,44,55]
# for i ,ll in enumerate(num,start=3):
#     if i >4 :
#         print(ll)
# x={'alo':2,'bbb':3}
# print(x.values())
#asdd = (ord(xx.keys()) for xx in x if xx.values() >1)
#aff = sum(asdd)
# print(ord('a'))

# leo = 'fasdf'
# for i in leo:
#     print(ord(i))
# if __name__ == '__main__':
#     zxcv = hee.funa(4)
#     print(zxcv(3))