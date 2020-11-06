# import sys

# def listadd(l1):
# 	l2 = []
# 	for data in l1:
# 		if data in l2:
# 			continue
# 		else:
# 			l2.append(data)
# 	return l2

# # l1 = input("Enter a list:")
# # li=[1,2,3,3,4,4,4,5,5]
# li = sys.argv[1:]
# print(listadd(li))

# n = int(input("Enter num:"))
# li=[]
# for i in range(1,n):
# 	if n%i==0:
# 		li.append(i)

# sum = 0
# for i in li:
# 	sum+=i
# if sum==n:

# 	print("perfect")

# n = int(input("Enter number of rows:"))
# a=[]
# for i in range(n):
# 	a.append([])
# 	a[i].append(1)
# 	for j in range(1,i):
# 		a[i].append(a[i-1][j-1]+a[i-1][j])
# 	if i!=0:
# 		a[i].append(1)
# for li in a:
# 	print(li)

# st = input("ENter your string:")

# small = []
# for i in range(97,123):
# 	small.append(chr(i))
# nums=[]
# for i in range(10):
# 	nums.append(str(i))

# l1=[]
# for letter in st:
# 	if letter.lower() in l1 or letter==' ' or letter in nums:
# 		pass
# 	else:
# 		l1.append(letter.lower())
# print(small)
# print(l1)
# if len(l1)==len(small):
# 	print("yesss... All alphabets present")
# else:
# 	print("All alphabets not there")

# st = input("Enter input:")

# l1=[]
# l1=st.split('-')

# l1 = sorted(l1)

# print('-'.join(l1))

# odd_num=[x for x in range(1,11) if x%2!=0]
# print(odd_num)

# starts_with=lambda x: True if x.startswith ('A') else False
# print(starts_with('Python'))

# s = lambda x:x*5
# n = int(input("Enter num:"))
# print(s(n))

# l1 = [('English',76),('Math',90),('SCience',87)]
# print("Before sort:",l1)
# l1.sort(key=lambda x:x[1])
# print("sorted:",l1)

# my_dict = [{'Name':'aditya','subject':'cse','mark':109},{'Name':'akash','subject':'math','mark':77},{'Name':'kumar','subject':'html','mark':90}]
# s = sorted(my_dict,key=lambda x:x['subject'],reverse=True)
# print(s)

# l1=["1","7","4","9","6"]
# l1.sort()
# print(l1)

# def calculate_sqr(n):
# 	return n*n
# 	number=(3,5,8,2)      
# result=map(calculate_sqr,number)
# print(result)

# for i in range(1,8):
# 	if i==7:
# 		print(i)
# 	else:
# 		print(i,end="-->")

# import os
# print("Operating system:",os.name)
# # print("Current os name:",os.uname())
# print("Current working directory:",os.getcwd())
# print("List of files and directories of current working directory:")
# print(os.listdir('.'))

# print("Test if a specified file exists or  not:")
# try:
# 	filename='abc.txt'
# 	f = open(filename,'r')
# 	data = f.read()
# 	print(data)
# 	f.close()
# except IOError:
# 	print("Unable to access file:",filename)

# print fruit values less than 30
# fruits = {'banana':20,'apple':40,'pineapple':50,'pomegram':24}

# for f,p in fruits.items():
# 	if p<30:
# 		print("{} : {}".format(f,p))

# import os

# path=input("Please enter path:")
# print("Directories:")
# print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))])
# print("Files:")
# print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path,name))])

# import os
# print("Exist?:",os.access("abc.txt",os.F_OK))
# print("Readable?:",os.access("abc.txt",os.R_OK))
# print("Writable?:",os.access("abc.txt",os.W_OK))
# print("Executable?:",os.access("abc.txt",os.X_OK))

# import os
# import time
# import sys
# path="D:"
# stat_info = os.stat(path)
# print("Path name:",path)
# print("Size:",stat_info.st_size)
# print("Permission:",stat_info.st_mode)
# print("Owner:",stat_info.st_uid)
# print("Device:",stat_info.st_dev)
# print("Created:",time.ctime(stat_info.st_ctime))
# print("Last modified:",time.ctime(stat_info.st_mtime))
# print("Last accessed:",time.ctime(stat_info.st_atime))

# for x in range(10):
# 	if x==9:
# 		print(x)
# 	else:
# 		print(x,end="-->")

# def check(s1,s2):
# 	if (sorted(s1)==sorted(s2)):
# 		print("Strings are anagram")
# 	else:
# 		print("Not anagram")
# s1="abc"
# s2="bdca"
# check(s1,s2)

# def convert(s):
# 	str1=""
# 	return(str1.join(s))
# s=['a','p','p','l','e']
# print(convert(s))

# def convert(s):
# 	str1=""
# 	return(str1.join(s))
# s=['python',' ','for',' ','every','one']
# print(convert(s))

# vegetables={'cabagge':20,'chilli':10,'santra':40,'cucumber':35}
# for v,p in vegetables.items():
# 	if p>30:
# 		print('{}:{}'.format(v,p))

# fruits={'apple':55,'orange':30,'quiee':60,'nuts':50}
# for f,p in fruits.items():
# 	if p>50:
# 		print('{}:{}'.format(f,p))

# def convert(s):
# 	str1=''
# 	return(str1.join(s))
# s=['a','','n',' ','t']
# print(convert(s))

# x=int(input("Enter a number:"))
# y=int(input("Enter a number:"))
# if x>y:
# 	print("The bigger no is:",x)
# else:
# 	print("x is not big")

# x=int(input("Enter x:"))
# y=int(input("Enter y:"))
# z=int(input("Enter z:"))
# if x>y and y>z:
# 	print("The bigger no is:",x)
# elif y>z:
# 	print("The bigger no is:",y)
# else:
# 	print("bigger no is:",z)

# n=int(input("Enter a number:"))
# if n>=0 and n<=100:
# 	print("the number",n ,"is inside 0 to 100")
# else:
# 	print("no is out of range")

# s="Akash"
# for x in s:
# 	print(x)

# for x in range(11):
# 	print(x)

# count=0
# for x in range(1,501):
# 	if (x%3==0 & x%7==0 & x%9==0):
# 		print(x)
# 		count+=1
# print("total nos are:",count)

# count=0
# for x in range(21):
# 	if(x%2!=0):
# 		print("Odd numbers are:",x)
# 		count+=1
# print("Total odd are",count)

# s=input("Enter a string:")
# i=0
# for x in s:
# 	print("the character persent at",i,"index is",x)
# 	i+=1


# s=input("Enter the string:")
# i=0
# for x in s:
# 	print("the character present in",i,"index is",x)
# 	i+=1

# for x in range(10,1,-1):
# 	print(x)

# list=eval(input("Enter the list:"))
# sum=0
# for x in list:
# 	sum+=x
# print("Sum of numbers is:",sum)

# list=eval(input("Enter a list:"))
# mul=1
# for x in list:
# 	mul=mul*x
# print("Multiplication of digits is:",mul)

# x=1
# while x<=10:
# 	print(x)
# 	x=x+1

# n=int(input("Enter any number:"))
# sum=0
# i=1
# while i<=n:
# 	sum=sum+i
# 	i=i+1
# print("sum of", n, "numbers is:",sum)

# books={'maths':100,'physics':200,'chem':160}
# for b,p in books.items():
# 	if p<150:
# 		print("{} : {}".format(b,p))

# for i in range(15):
# 	if i==10:
# 		print("Its enough, now break")
# 		break
# 	print(i)

# list=[100,200,300,400,500]
# for i in list:
# 	if i>300:
# 		print("Give the outputs")
# 		break
# 	print(i)

# for i in range(10):
# 	if i%2!=0:
# 		continue
# 	print(i)

# cart=[10,399,28,580,99]
# for item in cart:
# 	if item>=200:
# 		print("Cant process items:",item)
# 		continue
# 	print(item)

# count=0
# for x in range(1500,2701):
# 	if (x%7==0) and (x%5==0):
# 		print(x)
# 		count+=1
# print("numbers are",count)

# import json
# json_obj='{"Name":"John","Class":5,"Age":6}'
# python_obj=json.loads(json_obj)
# print("JSON_DATA:")
# print(python_obj)
# print("Name:",python_obj["Name"])
# print("Class:",python_obj["Class"])
# print("Age:",python_obj["Age"])

# import json
# python_obj={
# 	"Name":"Akash",
# 	"Class":7,
# 	"Marks":100
# }
# JSON_DATA=json.dumps(python_obj)
# print(JSON_DATA)

# import json
# python_list=["Apple","Banana","Guava"]
# python_str="A for Apple"
# python_dict={"Name":"John","Class":5,"Age":6}
# json_list=json.dumps(python_list)
# json_str=json.dumps(python_str)
# json_dict=json.dumps(python_dict)
# print("Json_List:",json_list)
# print("Json_Str:",json_str)
# print("Json_Dict:",json_dict)

# import json
# json_dict={"A":3,"H":22,"E":6}
# print(json_dict)
# print("JSON_DATA:")
# print(json.dumps(json_dict,sort_keys=True,indent=4))

# import json
# json_dict='{"Name":"John","Class":5,"Age":6}'
# json_str='"Apple is tasty"'
# python_dict=json.loads(json_dict)
# python_str=json.loads(json_str)
# print("python_Dict:",python_dict)
# print("python_Str:",python_str)

# from array import *
# array_num=array
# st = "abc123"
# l1 = []
# for i in st:
# 	    print(i)
# 	try:
# 		l1.append(int(i))
# 	except ValueError:
# 		continue
# print(l1)

# x = "malayalam"
# w = "" 
# for i in x: 
#     w = i + w 
#     if (x==w): 
#         print("YES")

# def reverse(str):
# 	return str[::-1]
# def check_Pallindrome(str):
# 	rev=reverse(str)
# 	if (str==rev):
# 		return True
# 	return False
# str="malayala"
# print(check_Pallindrome(str))

# l1=[9,6,4,2,3,4,5,3,6,7,7,8,9,5]
# res=[]
# for i in l1:
# 	if i not in res:
# 		res.append(i)
# print("List after remove duplicates:",res)
# print("Asscending order of list is:",sorted(res))

# s='python is very easy'
# l=s.split()
# print(l)
# l1=l[::-1]
# print(l1)
# s1=' '.join(l1)
# print(s1)

# s='durga'
# r=reversed(s)
# output=''.join(r)
# print(output)

# s='python is easy'
# l=s.split()
# l1=[]
# for word in l:
# 	l1.append(word[::-1])
# print(l1)

# s='one two three four five six'
# l=s.split()
# l1=[]
# i=0
# while i<len(l):
# 	if i%2==0:
# 		l1.append(l[i])
# 	else:
# 		l1.append(l[i][::-1])
# 	i=i+1
# output=' '.join(l1)
# print(output) 

# s='durgasoft'
# i=0
# print('Char present in even index is:')
# while i<len(s):
# 	print(s[i])
# 	i=i+2
# i=1
# print('Char present in odd index:')
# while i<len(s):
# 	print(s[i])
# 	i=i+2

# s='durgasoft'
# print('Char present in even index is:',s[0::2])
# print('Char present in odd index:',s[1::2])

# s='s9B2e0D4'
# alphabets=[]
# digits=[]
# for ch in s:
# 	if ch.isalpha():
# 		alphabets.append(ch)
# 	else:
# 		digits.append(ch)
# print(alphabets)
# print(digits)
# output=''.join(sorted(alphabets)+sorted(digits))
# print(output)

# s=input("Enter a string:")
# previous=s[0]
# c=1
# i=1
# output=''
# while i<len(s):
# 	if s[i]==previous:
# 		c=c+1
# 	else:
# 		output=output+str(c)+previous
# 		previous=s[i]
# 		c=1
# 	if i==len(s)-1:
# 		output=output+str(c)+previous
# 	i=i+1
# print(output)

# s=input("Enter a string:")
# output=''
# for ch in s:
# 	if ch.isalpha():
# 		x=ch
# 	else:
# 		d=int(ch)
# 		output=output+x*d
# print(output)

# s=input("Enter any string:")
# output=''
# for ch in s:
# 	if ch.isalpha():
# 		x=ch
# 	else:
# 		d=int(ch)
# 		output=output+d*x
# print(''.join(sorted(output)))

# print(ord('A'))
# print(chr(102))

# s=input("Enter a string:")
# output=''
# for ch in s:
# 	if ch.isalpha():
# 		output=output+ch
# 		x=ch
# 	else:
# 		d=int(ch)
# 		newch=chr(ord(x)+d)
# 		output=output+newch
# print(output)

# s=[9,4,2,6,5,8]
# output=''
# i=0
# if i in s:
# 	output=','.join(str(i)for i in s)
# print(output)


# str1 = input("Please enter your own String : ")
# if(str1 == str1[:: - 1]):
#    print("This is a Palindrome String")
# else:
#    print("This is Not a Palindrome String")
 
 # n=int(input("Enter the number of rows:"))
 # for i in range(1,n+1):
 # 	for j in range(1,i+1):
 # 		print("*",end=" ")
 # 	print()

 # def pal("str"):
 # 	x=str[::-1]
 # 	if x==num:
 # 		print("Pallindrome")
 # 	else:
 # 		print("Not Pallindrome")
 # print(pal("madam"))

# x=input("Enter a string:")
# if (x==x[::-1]):
# 	print("Palindrome")
# else:
# 	print("not a pallindrome")

# def fact(num):
# 	if num==1:
# 		return num
# 	else:
# 		return num*fact(num-1)
# print(fact(5))

# def fact(num):
# 	if num==1:
# 		return num
# 	else:
# 		return num*fact(num-1)
# print(fact(4))

# a=int(input("Enter first no:"))
# b=int(input("Enter second no:"))
# n=int(input("Enter no of elements:"))
# print(a,b,end=" ")
# while n-2:
# 	c=a+b
# 	a=b
# 	b=c
#     print(c,end=" ")
# 	n=n-1

# num=int(input("Eneter a no:"))
# sum=0
# temp=num
# while temp>0:
# 	c=temp%10
# 	sum+=c**3
# 	temp//=10
# if num==sum:
# 	print("Armstrong no")
# else:
# 	print("not an Armstrong no")

# year=int(input("Enter a year :"))
# if year%400==0:
# 	print("leap year")
# elif year%4==0:
# 	print("leap year")
# elif year%100==0:
# 	print("not a ly")
# else:
# 	print("not a lp yr")

# num=int(input("Enter a num:"))
# for i in range(2,num):
# 	if num%i==0:
# 		print("not prime")
# 		break
# 	else:
# 		print("prime one")
# 		break

# def check(s1,s2):
# 	if (sorted(s1)==sorted(s2)):
# 		print("Anagram")
# 	else:
# 		print("Not anagram")
# s1="abc"
# s2="bc"
# check(s1,s2)

# def convert(str):
# 	str1=''
# 	return(str1.join(str))
# str=['a','p','e']
# print(convert(str))

# def rev(s):
# 	str=""
# 	for i in s:
# 		str=i+str
# 	return str
# print(rev("apple"))

# str='Python is easy'
# l=str.split()
# l1=l[::-1]
# output=' '.join(l1)
# print(output)

# str="python is easy"
# l=str.split()
# l1=[]
# for ch in l:
# 	l1.append(ch[::-1])
# print(l1)
# output=' '.join(l1)
# print(output)

# s="AAABBBBCC"
# l=[]
# for ch in s:
# 	if ch not in l:
# 		l.append(ch)
# print(l)
# output=''.join(l)
# print(output)

# s=input("Some String:")
# l=[]
# for ch in s:
# 	if ch not in l:
# 		l.append(ch)
# for ch in sorted(l):
# 	print('{} occures {} times'.format(ch,s.count(ch)))

# s=input("Enter a string:")
# s1=set(s)
# for ch in sorted(s1):
# 	print('{} occurs {} times'.format(ch,s.count(ch)))

# d={}
# d['A']=100
# d['B']=200
# print(d)
# d['A']=300
# print(d)
# print(d.get('A'))
# print(d.get('Z'))
# print(d.get('B',0))
# print(d.get('D',0))
# d['A']=d.get('A',0)+1
# print(d)
# d['V']=d.get('V',0)+1
# print(d)

# d={'W': 300, 'A': 200, 'C':400}
# for k,v in d.items():
# 	print(k,v)

# d={'W': 300, 'A': 200, 'C':400}
# for k,v in sorted(d.items()):
# 	print(k,v)

# s=input("Enter a string:")
# d={}
# for ch in s:
# 	d[ch]=d.get(ch,0)+1
# print(d)
# for k,v in sorted(d.items()):
# 	print('{} occurs {} times'.format(k,v))

# s=input("Enter a string:")
# d={}
# for ch in s:
# 	d[ch]=d.get(ch,0)+1
# output=''
# for k,v in d.items():
# 	output=output+str(v)+k
# print(output)

# s=input("Enter a string:")
# d={}
# for ch in s:
# 	d[ch]=d.get(ch,0)+1
# output=''
# for k,v in sorted(d.items()):
# 	output=output+k+str(v)
# print(output)

# s=input("Enter a String:")
# d={}
# v={'a','e','i','o','u','A','E','I','O','U'}
# for ch in s:
# 	if ch in v:
# 		d[ch]=d.get(ch,0)+1
# for k,v in d.items():
# 	print('{} occurs {} times'.format(k,v))

list=[]
list=list(dict.fromkeys(list))
print(list)